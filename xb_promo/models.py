from django.db import models
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
    priority = models.IntegerField()
    description = models.CharField(max_length=240)
    keywords = models.CharField(max_length=240)
    content = models.TextField()
    screenshot_img = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['priority', 'date_submitted']

    def __str__(self):
        return self.title


class Answer(models.Model):
    title = models.CharField(max_length=80, unique=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='user_answer', null=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    priority = models.IntegerField()
    related_issue = models.ForeignKey(Issue, on_delete=models.CASCADE,
                                      related_name='issue_answer')
    content = models.TextField()
    screenshot_img = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['related_issue', 'priority', 'date_submitted']

    def __str__(self):
        return self.title
