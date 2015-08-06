# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('vat', models.CharField(max_length=11)),
                ('office', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('assigning', models.DateTimeField()),
                ('expiration', models.DateTimeField()),
                ('id_card', models.ForeignKey(to='user.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sellings',
            fields=[
                ('id_store', models.ForeignKey(primary_key=True, to='company.Stores')),
                ('id_item', models.ForeignKey(primary_key=True, serialize=False, to='company.Items')),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='stores',
            name='id_company',
            field=models.ForeignKey(to='company.Companies'),
        ),
        migrations.AddField(
            model_name='points',
            name='id_item',
            field=models.ForeignKey(to='company.Items'),
        ),
    ]
