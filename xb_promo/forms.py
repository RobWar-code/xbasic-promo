from django import forms
from django_summernote.widgets import SummernoteWidget
from cloudinary.forms import CloudinaryJsFileField
from .models import Issue, Answer


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
    title = forms.CharField(widget=forms.
                            TextInput(attrs={'style': 'width: 40%'}))
    description = forms.CharField(widget=forms.
                                  TextInput(attrs={'style': 'width: 80%'}))
    keywords = forms.CharField(widget=forms.
                               TextInput(attrs={'style': 'width: 81%'}))
    # screenshot_img = CloudinaryJsFileField()


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = (
            'title',
            'content',
            'screenshot_img'
        )

    widgets = {
        'content': SummernoteWidget(),
    }
    title = forms.CharField(widget=forms.
                            TextInput(attrs={'style': 'width: 40%'}))
