# Generated by Django 3.2.18 on 2023-05-03 14:35

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xb_promo', '0011_alter_issue_screenshot_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='screenshot_img',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
