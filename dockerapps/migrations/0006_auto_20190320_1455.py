# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-20 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("dockerapps", "0005_auto_20190314_0924")]

    operations = [
        migrations.AlterField(
            model_name="dockerapp",
            name="host_port",
            field=models.PositiveIntegerField(
                blank=True, help_text="Port used by the Docker image", null=True, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="dockerapp",
            name="internal_port",
            field=models.PositiveIntegerField(
                blank=True, help_text="Port used by the Docker image", null=True
            ),
        ),
        migrations.AlterField(
            model_name="dockerapp",
            name="state",
            field=models.CharField(
                choices=[
                    ("idle", "idle"),
                    ("starting", "starting"),
                    ("running", "running"),
                    ("stopping", "stopping"),
                    ("failed", "failed"),
                ],
                default="idle",
                help_text="The current docker container state",
                max_length=32,
            ),
        ),
    ]