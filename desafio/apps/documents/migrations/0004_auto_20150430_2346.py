# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20150430_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='user_group',
            field=models.ForeignKey(to='usergroups.UserGroup', blank=True),
            preserve_default=True,
        ),
    ]
