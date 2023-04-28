from django import forms
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.widgets import SummernoteWidget
from .models import FeaturePage, FeatureSection, Issue, Answer


class FeaturePageForm(forms.ModelForm):
    class Meta:
        model = FeaturePage
        fields = '__all__'


# Register your models here.
@admin.register(FeaturePage)
class FeaturePageAdmin(admin.ModelAdmin):
    form = FeaturePageForm
    prepopulated_fields = {'slug': ('page_name', )}


class FeatureSectionForm(forms.ModelForm):
    class Meta:
        model = FeatureSection
        fields = '__all__'


@admin.register(FeatureSection)
class SectionAdmin(admin.ModelAdmin):
    form = FeatureSectionForm
    list_display = ('feature_page', 'title')


class IssueAdminForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = '__all__'


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    form = IssueAdminForm
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'date_submitted')


class AnswerAdminForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    form = AnswerAdminForm
    search_fields = ['related_issue']
    list_display = ('related_issue', "title", "date_submitted")
