# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-15 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liefspelen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(default='../static/images/spelen.png', upload_to=''),
        ),
    ]
