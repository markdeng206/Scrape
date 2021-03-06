# Generated by Django 2.2 on 2020-03-21 07:25

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('publisher', models.CharField(blank=True, max_length=255, null=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), blank=True, null=True, size=None)),
                ('url', models.CharField(max_length=255, unique=True)),
                ('isbn', models.CharField(max_length=255, unique=True)),
                ('cover', models.CharField(blank=True, max_length=255, null=True)),
                ('page_number', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('score', models.FloatField(blank=True, null=True)),
                ('introduction', models.TextField(blank=True, null=True)),
                ('catalog', models.TextField(blank=True, null=True)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, max_length=255, null=True)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='app.Person'),
        ),
    ]
