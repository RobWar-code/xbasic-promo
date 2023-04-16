from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Issue


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = (
            'title',
            'description',
            'keywords',
            'content',
            'screenshot_img'
        )

    widgets = {
        'content': SummernoteWidget(),
    }
    description = forms.CharField(widget=forms.
                                  TextInput(attrs={'style': 'width: 80%'}))
    keywords = forms.CharField(widget=forms.
                               TextInput(attrs={'style': 'width: 81%'}))
