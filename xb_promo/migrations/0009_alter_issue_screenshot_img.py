# Generated by Django 3.2.18 on 2023-04-17 17:05

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xb_promo', '0008_alter_issue_search_vector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='screenshot_img',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]