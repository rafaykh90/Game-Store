# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-18 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtest', '0007_games_salescount'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedgame',
            name='highScore',
            field=models.IntegerField(default=0),
        ),
    ]
