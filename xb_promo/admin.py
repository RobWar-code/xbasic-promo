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


class SectionAdmin(SummernoteModelAdmin):
    summernote_fields = ('article')
    list_display = ('feature_page', 'title')


admin.site.register(FeatureSection, SectionAdmin)


@admin.register(Issue)
class IssueAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'date_submitted')


@admin.register(Answer)
class AnswerAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    search_fields = ['related_issue']
    list_display = ('related_issue', "title", "date_submitted")
