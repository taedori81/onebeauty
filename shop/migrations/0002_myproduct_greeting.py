# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myproduct',
            name='greeting',
            field=models.CharField(default='Hello World', max_length=255),
        ),
    ]
