from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib.postgres.search import SearchQuery, SearchRank
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
        elif issue_num > num_issues:
            issue_num = num_issues - 1
        issue = queryset[issue_num]
        answer_set = issue.issue_answer.all()
        num_answers = len(answer_set)
        if 'answer_num' not in kwargs:
            answer_num = 0
        else:
            answer_num = kwargs['answer_num']
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
