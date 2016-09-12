# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-07 02:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('internships', '0003_auto_20160907_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_type', models.IntegerField(choices=[(0, 'deadline passed'), (1, 'followup'), (2, 'successful'), (3, 'interviewing'), (4, 'post interview'), (5, 'rejected'), (6, 'todo'), (7, 'waiting')])),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=400)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('application_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internships.ApplicationStatus')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internships.Company')),
            ],
        ),
    ]