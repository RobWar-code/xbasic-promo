from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Issue


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ('title', 'content')

    widgets = {
        'content': SummernoteWidget()
    }
