# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ignityLinks', '0002_auto_20190717_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='novolink',
            name='cliques',
            field=models.IntegerField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
