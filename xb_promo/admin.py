from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import FeaturePage, FeatureSection, Issues, Answers


# Register your models here.
@admin.register(FeaturePage)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('page_name', )}
    summernote_fields = ('page_intro')


@admin.register(FeatureSection)
class SectionAdmin(SummernoteModelAdmin):
    summernote_fields = ('article')
    list_display = ('feature_page', 'title')


@admin.register(Issues)
class IssueAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    list_display = ('title', 'date_submitted')


@admin.register(Answers)
class AnswerAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    list_display = ('related_issue', "title", "date_submitted")
