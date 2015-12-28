# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20151217_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='myproduct',
            name='rating',
            field=models.FloatField(verbose_name='Rating', editable=False, null=True),
        ),
    ]
