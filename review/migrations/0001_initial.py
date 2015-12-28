# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('value', models.CharField(null=True, blank=True, choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], max_length=20, verbose_name='Value')),
            ],
            options={
                'ordering': ['category', 'review'],
            },
        ),
        migrations.CreateModel(
            name='RatingCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('identifier', models.SlugField(blank=True, max_length=32, verbose_name='Identifier')),
                ('counts_for_average', models.BooleanField(verbose_name='Counts for average rating', default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RatingCategoryChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('value', models.CharField(null=True, blank=True, max_length=20, verbose_name='Value')),
                ('ratingcategory', models.ForeignKey(to='review.RatingCategory', verbose_name='Rating category', related_name='choices')),
            ],
            options={
                'ordering': ('-value',),
            },
        ),
        migrations.CreateModel(
            name='RatingCategoryChoiceTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('label', models.CharField(max_length=128, verbose_name='Label')),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(null=True, to='review.RatingCategoryChoice', editable=False, related_name='translations')),
            ],
            options={
                'default_permissions': (),
                'db_table': 'review_ratingcategorychoice_translation',
                'db_tablespace': '',
                'managed': True,
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RatingCategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('question', models.CharField(null=True, blank=True, max_length=512)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(null=True, to='review.RatingCategory', editable=False, related_name='translations')),
            ],
            options={
                'default_permissions': (),
                'db_table': 'review_ratingcategory_translation',
                'db_tablespace': '',
                'managed': True,
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('object_id', models.PositiveIntegerField()),
                ('content', models.TextField(blank=True, max_length=1024, verbose_name='Content')),
                ('headline', models.CharField(blank=True, max_length=255, verbose_name='Headline')),
                ('language', models.CharField(blank=True, max_length=5, verbose_name='Language')),
                ('creation_date', models.DateTimeField(verbose_name='Creation date', auto_now_add=True)),
                ('average_rating', models.FloatField(verbose_name='Average rating', default=0)),
                ('extra_object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('extra_content_type', models.ForeignKey(null=True, to='contenttypes.ContentType', blank=True, related_name='reviews_attached')),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, verbose_name='User', blank=True)),
            ],
            options={
                'ordering': ['-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='ReviewExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('type', models.CharField(max_length=256, verbose_name='Type')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('review', models.ForeignKey(to='review.Review', verbose_name='Review')),
            ],
            options={
                'ordering': ['type'],
            },
        ),
        migrations.AddField(
            model_name='rating',
            name='category',
            field=models.ForeignKey(to='review.RatingCategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='rating',
            name='review',
            field=models.ForeignKey(to='review.Review', verbose_name='Review', related_name='ratings'),
        ),
        migrations.AlterUniqueTogether(
            name='ratingcategorytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='ratingcategorychoicetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
