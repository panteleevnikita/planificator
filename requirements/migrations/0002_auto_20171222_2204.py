# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-22 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20171222_2204'),
        ('clients', '0002_auto_20171222_2204'),
        ('requirements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clients.Client'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assessment',
            name='requirement',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='requirements.Requirement'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='generalrequirement',
            name='projects',
            field=models.ManyToManyField(to='projects.Project'),
        ),
        migrations.AddField(
            model_name='requirement',
            name='assessments',
            field=models.ManyToManyField(through='requirements.Assessment', to='clients.Client'),
        ),
        migrations.AddField(
            model_name='requirement',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
            preserve_default=False,
        ),
    ]