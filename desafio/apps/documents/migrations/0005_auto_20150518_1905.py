# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_auto_20150430_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='user_group',
            field=models.ForeignKey(blank=True, to='usergroups.UserGroup', null=True),
            preserve_default=True,
        ),
    ]
