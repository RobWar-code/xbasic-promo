# Generated by Django 3.2.18 on 2023-04-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xb_promo', '0005_auto_20230410_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='priority',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.IntegerField(default=3),
        ),
    ]
