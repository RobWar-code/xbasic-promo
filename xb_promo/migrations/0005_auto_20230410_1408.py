# Generated by Django 3.2.18 on 2023-04-10 14:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('xb_promo', '0004_answers_issues'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answers',
            new_name='Answer',
        ),
        migrations.RenameModel(
            old_name='Issues',
            new_name='Issue',
        ),
    ]