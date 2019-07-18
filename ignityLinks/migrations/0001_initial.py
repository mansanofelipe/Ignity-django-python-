# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NovoForm',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NovoLink',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('data_criacao', models.CharField(max_length=255)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
