# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-14 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("dockerapps", "0003_auto_20190314_0823")]

    operations = [
        migrations.RenameField(model_name="dockerapp", old_name="port", new_name="host_port"),
        migrations.AddField(
            model_name="dockerapp",
            name="internal_port",
            field=models.PositiveIntegerField(
                blank=True, help_text="Port used by the Docker image", null=True, unique=True
            ),
        ),
    ]
