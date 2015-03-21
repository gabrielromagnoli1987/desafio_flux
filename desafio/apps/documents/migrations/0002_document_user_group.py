# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usergroups', '0001_initial'),
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='user_group',
            field=models.ForeignKey(to='usergroups.UserGroup'),
            preserve_default=True,
        ),
    ]
