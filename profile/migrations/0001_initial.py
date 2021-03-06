# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 02:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nickname', models.CharField(blank=True, default='', max_length=16)),
                ('sex', models.IntegerField(default=0)),
                ('phone', models.CharField(blank=True, default='', max_length=16)),
                ('department', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='company.Department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
                'get_latest_by': 'created',
            },
        ),
    ]
