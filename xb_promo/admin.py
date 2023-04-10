from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import FeaturePage, FeatureSection, Issue, Answer


# Register your models here.
@admin.register(FeaturePage)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('page_name', )}
    summernote_fields = ('page_intro')


@admin.register(FeatureSection)
class SectionAdmin(SummernoteModelAdmin):
    summernote_fields = ('article')
    list_display = ('feature_page', 'title')


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
