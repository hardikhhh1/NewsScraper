# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HackerNews', '0002_auto_20150228_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='storymodel',
            name='is_interested',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
