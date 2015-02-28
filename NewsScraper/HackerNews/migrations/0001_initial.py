# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoryComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_link', models.URLField(max_length=500)),
                ('comment', models.CharField(default=b'', max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoryModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=100)),
                ('link', models.URLField(default=b'')),
                ('domain', models.CharField(default=b'', max_length=200)),
                ('points', models.IntegerField()),
                ('submitter', models.CharField(default=b'', max_length=100)),
                ('published_time', models.TimeField()),
                ('num_comments', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Story',
                'verbose_name_plural': 'Stories',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='storycomments',
            name='story',
            field=models.ForeignKey(to='HackerNews.StoryModel'),
            preserve_default=True,
        ),
    ]
