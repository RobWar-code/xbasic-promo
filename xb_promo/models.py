from django.db import models
from django.contrib.postgres.search import SearchVector, SearchVectorField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.indexes import GinIndex
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
# See: /doc/project-analysis.txt for a description of the models
class FeaturePage(models.Model):
    page_name = models.CharField(max_length=80, unique=True)
    page_title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    page_intro = models.TextField(null=True, blank=True)
    excerpt = models.CharField(max_length=80, blank=True)
    intro_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.page_name


class FeatureSection(models.Model):
    title = models.CharField(max_length=80, unique=True)
    section_number = models.IntegerField()
    feature_page = models.ForeignKey(FeaturePage, on_delete=models.CASCADE,
                                     related_name='section')
    article = models.TextField()
    excerpt = models.CharField(max_length=80, blank=True)
    section_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['feature_page', 'section_number']


class Issue(models.Model):
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='user_issue', null=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=3)
    description = models.CharField(max_length=240)
    keywords = models.CharField(max_length=240)
    content = models.TextField()
    screenshot_img = CloudinaryField('image', default='placeholder',
                                     blank=True)
    search_vector = SearchVectorField(null=True, blank=True)

    class Meta:
        ordering = ['priority', '-date_submitted']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk is not None:
            self.set_search_vector()
        super().save(*args, **kwargs)

    def set_search_vector(self):
        self.search_vector = (
            SearchVector("title", weight="A")
            + SearchVector("keywords", weight="B")
            + SearchVector("description", weight="C")
        )
        Issue.objects.filter(pk=self.pk).\
            update(search_vector=models.F('search_vector'))


class Answer(models.Model):
    title = models.CharField(max_length=80, unique=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='user_answer', null=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=3)
    related_issue = models.ForeignKey(Issue, on_delete=models.CASCADE,
                                      related_name='issue_answer')
    content = models.TextField()
    screenshot_img = CloudinaryField('image', default='placeholder',
                                     blank=True)

    class Meta:
        ordering = ['related_issue', 'priority', '-date_submitted']

    def __str__(self):
        return self.title
