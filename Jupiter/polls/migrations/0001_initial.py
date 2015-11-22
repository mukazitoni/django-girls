# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('price', models.IntegerField(max_length=4)),
                ('quality', models.CharField(max_length=5)),
                ('quantity', models.IntegerField(max_length=6)),
                ('colour', models.CharField(max_length=7)),
            ],
        ),
    ]
