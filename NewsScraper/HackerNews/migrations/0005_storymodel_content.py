# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HackerNews', '0004_storymodel_story_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='storymodel',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
