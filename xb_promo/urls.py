from . import views
from django.urls import path

urlpatterns = [
     path('', views.Feature.as_view(), name='home'),
     path('<slug:slug>', views.Feature.as_view(), name='feature_page'),
     path('issues/', views.IssueDisplay.as_view(), name='issue_display'),
     path('issues/<int:issue_num>/<int:answer_num>/<str:search_field>/\
<int:scroll_to_answer>/<int:scroll_delay>',
          views.IssueDisplay.as_view(), name='step_issue'),
     path('edit_issue/<int:edit>/<int:issue_num>/\
<str:search_field>/<int:issue_id>/',
          views.IssueEdit.as_view(), name='edit_issue'),
     path('add_issue/', views.IssueAdd.as_view(), name='add_issue'),
     path('delete_issue/<int:issue_id>/', views.delete_issue,
          name='delete_issue'),
     path('add_answer/<int:issue_id>/', views.AnswerAdd.as_view(),
          name="add_answer"),
     path('edit_answer/<int:issue_id>/<int:answer_id>/',
          views.AnswerEdit.as_view(), name="edit_answer"),
     path('delete_answer/<int:issue_id>/<int:answer_id>/',
          views.delete_answer, name='delete_answer'),
     path('dump_database/', views.DumpDatabase.as_view(), name='dump_database')
]
