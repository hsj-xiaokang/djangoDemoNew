# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-25 09:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=50, unique=True)),
                ('bpub_date', models.DateField()),
                ('bread', models.IntegerField(default=0)),
                ('bcomment', models.IntegerField(default=0)),
                ('idDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=50)),
                ('hgender', models.BooleanField(default=False)),
                ('isDelete', models.BooleanField(default=False)),
                ('hcontent', models.CharField(max_length=500)),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.BookInfo')),
            ],
        ),
    ]
