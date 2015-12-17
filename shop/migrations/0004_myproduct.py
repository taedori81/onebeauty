# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shoop', '0011_merge'),
        ('shop', '0003_auto_20151216_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('product', annoying.fields.AutoOneToOneField(to='shoop.Product')),
            ],
        ),
    ]
