# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HackerNews', '0003_storymodel_is_interested'),
    ]

    operations = [
        migrations.AddField(
            model_name='storymodel',
            name='story_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
