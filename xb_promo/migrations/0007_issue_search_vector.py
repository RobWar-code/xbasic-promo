# Generated by Django 3.2.18 on 2023-04-13 17:18

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xb_promo', '0006_auto_20230411_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
    ]
