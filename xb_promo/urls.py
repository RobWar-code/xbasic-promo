from . import views
from django.urls import path

urlpatterns = [
    path('', views.Feature.as_view(), name='home')
]
