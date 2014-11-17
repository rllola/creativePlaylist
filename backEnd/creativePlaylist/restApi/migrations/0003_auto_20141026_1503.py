# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restApi', '0002_auto_20141012_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='art',
            field=models.ForeignKey(related_name=b'art', to='restApi.Art'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(related_name=b'artist', to='restApi.Artist'),
        ),
    ]
