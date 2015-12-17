# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_myproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myproduct',
            name='product',
            field=annoying.fields.AutoOneToOneField(related_name='myproduct', to='shoop.Product'),
        ),
    ]
