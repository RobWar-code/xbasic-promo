# Generated by Django 3.2.18 on 2023-05-06 19:06

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xb_promo', '0015_alter_answer_screenshot_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='screenshot_img',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
