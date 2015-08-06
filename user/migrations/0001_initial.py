# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('card', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('city', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('cellphone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
