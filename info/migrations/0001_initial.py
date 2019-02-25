# Generated by Django 2.1.7 on 2019-02-24 20:52

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import rest_framework.compat


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('year', models.IntegerField(blank=True, null=True, validators=[rest_framework.compat.MinValueValidator(0)])),
                ('rated', models.CharField(blank=True, max_length=64, null=True)),
                ('released', models.CharField(blank=True, max_length=64, null=True)),
                ('runtime', models.CharField(blank=True, max_length=64, null=True)),
                ('genre', models.CharField(blank=True, max_length=64, null=True)),
                ('director', models.CharField(blank=True, max_length=512, null=True)),
                ('writer', models.CharField(blank=True, max_length=512, null=True)),
                ('actors', models.TextField(blank=True, null=True)),
                ('plot', models.TextField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=64, null=True)),
                ('country', models.CharField(blank=True, max_length=64, null=True)),
                ('awards', models.CharField(blank=True, max_length=512, null=True)),
                ('poster', models.TextField(blank=True, null=True)),
                ('ratings', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('metascore', models.CharField(blank=True, max_length=64, null=True)),
                ('imdbrating', models.CharField(blank=True, max_length=64, null=True)),
                ('imdbvotes', models.CharField(blank=True, max_length=64, null=True)),
                ('imdbid', models.CharField(blank=True, max_length=64, null=True)),
                ('type', models.CharField(blank=True, max_length=64, null=True)),
                ('dvd', models.CharField(blank=True, max_length=64, null=True)),
                ('boxoffice', models.CharField(blank=True, max_length=512, null=True)),
                ('production', models.CharField(blank=True, max_length=512, null=True)),
                ('website', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='info.Movie'),
        ),
    ]
