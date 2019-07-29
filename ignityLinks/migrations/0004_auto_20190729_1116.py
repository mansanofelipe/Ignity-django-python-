# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ignityLinks', '0003_novolink_cliques'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novolink',
            name='cliques',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
    ]
