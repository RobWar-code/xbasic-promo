import time
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic, View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.utils.text import slugify
from django.contrib.postgres.search import SearchVector, SearchQuery,\
    SearchRank
from django.contrib import messages
from django.db.models import F
import cloudinary.uploader
from .models import FeaturePage, Issue, Answer
from .forms import IssueForm, AnswerForm


# Features
class Feature(View):
    def get(self, request, slug=None, *args, **kwargs):
        if slug is None:
            slug = "xbasic-intro"

        queryset = FeaturePage.objects.all()
        feature_page = get_object_or_404(queryset, slug=slug)
        feature_sections = feature_page.section.order_by('section_number')
        return render(
            request,
            'index.html',
            {
                'feature_page': feature_page,
                'feature_sections': feature_sections
            }
        )


# Issues
class IssueDisplay(View):
    def get(self, request, *args, **kwargs):
        search_field = "X"
        # Initial Entry to Page
        if 'search_field' in kwargs:
            search_field = kwargs['search_field']  # Indicates no search field
        if request.GET.get('issue_search'):
            search_field = request.GET.get('issue_search')
            if not search_field:
                search_field = "X"

        if search_field != "X":
            query = SearchQuery(search_field)
            queryset = Issue.objects.annotate(
                rank=SearchRank('search_vector', query)).order_by('-rank')
        else:
            queryset = Issue.objects.all().order_by('priority',
                                                    '-date_submitted')

        if 'issue_num' not in kwargs:
            issue_num = 0
        else:
            issue_num = kwargs['issue_num']
        num_issues = len(queryset)
        if issue_num < 0:
            issue_num = 0
        elif issue_num >= num_issues:
            issue_num = num_issues - 1
        issue = queryset[issue_num]
        answer_set = issue.issue_answer.all().order_by('priority',
                                                       '-date_submitted')
        num_answers = len(answer_set)
        if 'answer_num' not in kwargs:
            answer_num = 0
        else:
            answer_num = kwargs['answer_num']
        if num_answers == 0:
            answer_num = 0
            answer = None
        else:
            if answer_num < 0:
                answer_num = 0
            elif answer_num >= num_answers:
                answer_num = num_answers - 1
            answer = answer_set[answer_num]

        return render(
            request,
            'issues.html',
            {
                'search_field': search_field,
                'num_issues': num_issues,
                'num_answers': num_answers,
                'issue_num': issue_num,
                'issue': issue,
                'answer_num': answer_num,
                'answer': answer,
                'timestamp': int(time.time())
            }
        )


class IssueEdit(View):
    def get(self, request, *args, **kwargs):
        # Keyword arguments are: issue_num, search_field
        search_field = kwargs['search_field']
        if search_field == "X":  # Empty search field
            queryset = Issue.objects.all()
        else:
            query = SearchQuery(search_field)
            queryset = Issue.objects.annotate(
                rank=SearchRank('search_vector', query)).order_by('-rank')

        issue_num = kwargs['issue_num']
        issue = queryset[issue_num]
        issue_id = issue.id
        issue = get_object_or_404(Issue, pk=issue_id)
        form = IssueForm(instance=issue)
        return render(request, 'edit_issue.html',
                      {'form': form,
                       'edit': 1,
                       'issue_num': issue_num,
                       'search_field': search_field,
                       'issue_id': issue_id})

    def post(self, request, *args, **kwargs):
        issue_num = kwargs['issue_num']
        search_field = kwargs['search_field']
        issue_id = kwargs['issue_id']
        issue = get_object_or_404(Issue, pk=issue_id)
        # Update record
        issue_form = IssueForm(request.POST, instance=issue)
        if issue_form.is_valid():
            instance = issue_form.save(commit=False)

            if 'screenshot_img' in request.FILES:
                # Upload the file to Cloudinary
                uploaded_file = cloudinary.uploader.\
                    upload(request.FILES['screenshot_img'])

                # Assign the Cloudinary URL to the `image` field of the `Issue`
                # model instance
                instance.screenshot_img = uploaded_file['url']

            instance.save()

            message_text = "Issue Updated Successfully!"
            messages.success(request, message_text)

            answer_num = 0
            return redirect('step_issue', issue_num=issue_num,
                            answer_num=answer_num, search_field=search_field)

        # Check for duplicate title
        message_text = issue_form.errors.get('title', None)
        messages.warning(request, message_text)
        form = IssueForm(instance=issue)
        return render(request, 'edit_issue.html',
                      {'form': form,
                       'edit': 1,
                       'issue_num': issue_num,
                       'search_field': search_field,
                       'issue_id': issue_id})


class IssueAdd(View):
    def get(self, request, *args, **kwargs):
        form = IssueForm()
        return render(request, 'edit_issue.html', {'form': form, 'edit': 0})

    def post(self, request, *args, **kwargs):
        issue_form = IssueForm(request.POST)
        if issue_form.is_valid():
            instance = issue_form.save(commit=False)
            instance.slug = slugify(instance.title)
            instance.author = request.user
            if 'screenshot_img' in request.FILES:
                # Upload the file to Cloudinary
                uploaded_file = cloudinary.uploader.\
                    upload(request.FILES['screenshot_img'])

                # Assign the Cloudinary URL to the `image` field of the `Issue`
                # model instance
                instance.screenshot_img = uploaded_file['url']

            instance.save()
            # Get the saved record and resave so that we can update search
            # vector
            title = instance.title
            issue_record = get_object_or_404(Issue, title=title)
            issue_record.save()

            message_text = "Issue Added Successfully!"
            messages.success(request, message_text)

            # Fetch this record to be represented on the issue display
            title = issue_form.cleaned_data['title']
            search_field = title
            issue_num = 0
            answer_num = 0
            return redirect('step_issue', issue_num=issue_num,
                            answer_num=answer_num, search_field=search_field)

        return render(request, 'edit_issue.html',
                      {'form': issue_form, 'edit': 0})


@csrf_exempt
def delete_issue(request, issue_id):
    try:
        issue = Issue.objects.get(id=issue_id)
        issue.delete()
        message_text = "Delete Issue Successful!"
        messages.success(request, message_text)
        # Add time stamp to overcome caching
        redirect_url = reverse('issue_display') + f'?t={int(time.time())}'
        return JsonResponse({
            'success': True,
            'redirect_url': f'{redirect_url}'
        })
    except Issue.DoesNotExist:
        message_text = "Delete Issue Failed!"
        messages.error(request, message_text)
        return JsonResponse({'success': False,
                             'error': 'Record does not exist'})


# Answers
class AnswerAdd(View):
    def get(self, request, *args, **kwargs):
        issue_id = kwargs['issue_id']
        issue = get_object_or_404(Issue, id=issue_id)
        form = AnswerForm()
        return render(
            request,
            "edit_answer.html",
            {
                'form': form,
                'edit': 0,
                'issue': issue,
                'issue_id': issue.id
            }
        )

    def post(self, request, *args, **kwargs):
        issue_id = kwargs["issue_id"]
        issue = get_object_or_404(Issue, id=issue_id)
        answer_form = AnswerForm(request.POST, request.FILES)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.author = request.user
            answer.related_issue = issue
            if 'screenshot_img' in request.FILES:
                # Upload the file to Cloudinary
                uploaded_file = cloudinary.uploader.\
                    upload(request.FILES['screenshot_img'])

                # Assign the Cloudinary URL to the `image` field of the `Issue`
                # model instance
                answer.screenshot_img = uploaded_file['url']
            answer.save()

            message_text = "Answer Added Successfully!"
            messages.success(request, message_text)

            # Get the details for the issue display
            search_field = issue.title
            issue_num = 0
            answer_num = 0
            return redirect('step_issue', issue_num=issue_num,
                            answer_num=answer_num, search_field=search_field)

        return redirect('add_answer', issue_id=issue_id)


class AnswerEdit(View):
    def get(self, request, *args, **kwargs):
        issue_id = kwargs['issue_id']
        answer_id = kwargs['answer_id']
        issue = get_object_or_404(Issue, id=issue_id)
        answer = get_object_or_404(Answer, id=answer_id)
        form = AnswerForm(instance=answer)
        return render(
            request,
            "edit_answer.html",
            {
                'form': form,
                'edit': 1,
                'issue': issue,
                'issue_id': issue_id,
                'answer_id': answer_id
            }
        )

    def post(self, request, *args, **kwargs):
        # Update the answer table
        issue_id = kwargs["issue_id"]
        answer_id = kwargs["answer_id"]
        issue = get_object_or_404(Issue, id=issue_id)
        answer = get_object_or_404(Answer, id=answer_id)
        answer_form = AnswerForm(request.POST, instance=answer)
        if answer_form.is_valid():
            instance = answer_form.save(commit=False)
            if 'screenshot_img' in request.FILES:
                # Upload the file to Cloudinary
                uploaded_file = cloudinary.uploader.\
                    upload(request.FILES['screenshot_img'])

                # Assign the Cloudinary URL to the `image` field of the `Issue`
                # model instance
                instance.screenshot_img = uploaded_file['url']

            instance.save()
        else:
            message_text = answer_form.errors.get('title', None)
            messages.warning(request, message_text)
            return redirect('edit_answer', issue_id=issue_id,
                            answer_id=answer_id)

        # Redirect to the step_issue issue display
        search_field = issue.title
        # Get the set of answers that applies to this issue
        answer_set = Answer.objects.filter(related_issue=issue)
        # Loop through the set and identify what position the
        # current answer is in
        for answer_num, answer in enumerate(answer_set):
            if answer.id == answer_id:
                break
        issue_num = 0

        message_text = "Answer Updated Successfully!"
        messages.success(request, message_text)

        return redirect("step_issue", issue_num=issue_num,
                        answer_num=answer_num, search_field=search_field)


@csrf_exempt
def delete_answer(request, issue_id, answer_id):
    try:
        answer = Answer.objects.get(id=answer_id)
        answer.delete()
        message_text = "Delete Answer Successful!"
        messages.success(request, message_text)
        # Get the issue to redisplay
        issue = Issue.objects.get(id=issue_id)
        search_field = issue.title
        redirect_url = reverse('step_issue',
                               kwargs={'issue_num': 0, 'answer_num': 0,
                                       'search_field': search_field})
        return JsonResponse({
            'success': True,
            'redirect_url': f'{redirect_url}'
        })
    except Answer.DoesNotExist:
        message_text = "Delete Answer Failed!"
        messages.error(request, message_text)
        return JsonResponse({'success': False,
                             'error': 'Answer record does not exist'})
