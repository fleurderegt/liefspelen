# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-04 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100)),
                ('cat_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('env_name', models.CharField(max_length=100)),
                ('env_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('min_age', models.IntegerField()),
                ('max_age', models.IntegerField()),
                ('min_players', models.IntegerField()),
                ('max_players', models.IntegerField()),
                ('categories', models.ManyToManyField(to='liefspelen.Category')),
                ('environments', models.ManyToManyField(to='liefspelen.Environment')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mat_name', models.CharField(max_length=100)),
                ('mat_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_name', models.CharField(max_length=100)),
                ('season_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
                ('tag_desc', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='materials',
            field=models.ManyToManyField(to='liefspelen.Material'),
        ),
        migrations.AddField(
            model_name='game',
            name='seasons',
            field=models.ManyToManyField(to='liefspelen.Season'),
        ),
        migrations.AddField(
            model_name='game',
            name='tags',
            field=models.ManyToManyField(to='liefspelen.Tag'),
        ),
    ]