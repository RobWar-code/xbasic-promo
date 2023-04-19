from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.utils.text import slugify
from django.contrib.postgres.search import SearchVector, SearchQuery,\
    SearchRank
from django.db.models import F
from .models import FeaturePage, Issue, Answer
from .forms import IssueForm


# Create your views here.
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
            queryset = Issue.objects.all()

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
        answer_set = issue.issue_answer.all()
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
                'answer': answer
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
            issue_form.save()
            answer_num = 0
            return redirect('step_issue', issue_num=issue_num,
                            answer_num=answer_num, search_field=search_field)

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
            instance.save()
            # Get the saved record and resave so that we can update search
            # vector
            title = instance.title
            issue_record = get_object_or_404(Issue, title=title)
            issue_record.save()

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
        Issue.objects.get(id=issue_id)
        issue.delete()
        return redirect('issue_display')
    except Issue.DoesNotExist:
        return JsonResponse({'success': False,
                             'error': 'Record does not exist'})
