from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import FeaturePage


# Register your models here.
@admin.register(FeaturePage)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('page_name', )}
    summernote_fields = ('page_intro')
