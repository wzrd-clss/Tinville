# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0005_auto_20150116_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='promoter',
            field=models.ForeignKey(verbose_name=b'Promoter', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
