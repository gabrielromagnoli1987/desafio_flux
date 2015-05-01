# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_document_user_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='path',
        ),
        migrations.AddField(
            model_name='document',
            name='file',
            field=models.FileField(default=datetime.datetime(2015, 4, 30, 22, 33, 18, 308143, tzinfo=utc), upload_to=b''),
            preserve_default=False,
        ),
    ]
