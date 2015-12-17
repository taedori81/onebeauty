# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_myproduct_greeting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myproduct',
            name='product',
        ),
        migrations.DeleteModel(
            name='MyProduct',
        ),
    ]
