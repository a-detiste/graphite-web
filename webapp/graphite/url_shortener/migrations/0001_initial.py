# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 11:22
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
