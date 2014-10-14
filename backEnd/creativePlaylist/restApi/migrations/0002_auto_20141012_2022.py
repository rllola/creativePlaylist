# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='submitedByUser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='art',
            name='artImage',
            field=models.ImageField(upload_to=b'art_image'),
        ),
        migrations.AlterField(
            model_name='art',
            name='artThumb',
            field=models.ImageField(upload_to=b'art_thumb'),
        ),
    ]
