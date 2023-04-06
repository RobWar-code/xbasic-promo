from . import views
from django.urls import path

urlpatterns = [
    path('', views.Feature.as_view(), name='home'),
    path('<slug:slug>', views.Feature.as_view(), name='feature_page')
]
