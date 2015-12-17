# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20151216_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myproduct',
            name='product',
            field=models.OneToOneField(to='shoop.Product'),
        ),
    ]
