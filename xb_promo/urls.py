from . import views
from django.urls import path

urlpatterns = [
    path('', views.Feature.as_view(), name='home'),
    path('<slug:slug>', views.Feature.as_view(), name='feature_page'),
    path('issues/', views.IssueDisplay.as_view(), name='issue_display'),
    path('issues/<int:issue_num>/<int:answer_num>/<str:search_field>/',
         views.IssueDisplay.as_view(), name='step_issue'),
]
