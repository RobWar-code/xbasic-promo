from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import FeaturePage, Issue, Answer


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
        if 'issue_num' not in kwargs:
            issue_num = 0
        else:
            issue_num = kwargs['issue_num']
        queryset = Issue.objects.all()
        if issue_num < 0:
            issue_num = 0
        elif issue_num > len(queryset):
            issue_num = len(queryset) - 1
        issue = queryset[issue_num]
        answer_set = issue.issue_answer.all()
        if 'answer_num' not in kwargs:
            answer_num = 0
        else:
            answer_num = kwargs['answer_num']
        if answer_num < 0:
            answer_num = 0
        elif answer_num > len(answer_set):
            answer_num = len(answer_set) - 1
        answer = answer_set[answer_num]
        return render(
            request,
            'issues.html',
            {
                'issue_num': 0,
                'issue': issue,
                'answer_num': 0,
                'answer': answer
            }
        )
