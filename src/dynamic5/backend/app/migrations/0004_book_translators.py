# Generated by Django 2.2 on 2020-03-21 13:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200321_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='translators',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), blank=True, null=True, size=None),
        ),
    ]