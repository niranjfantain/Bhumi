# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eventName', models.CharField(max_length=50, verbose_name=b'Event Name')),
                ('desc', models.TextField(max_length=150, verbose_name=b'Description')),
                ('eventType', models.CharField(default=b'I', max_length=2, verbose_name=b'Event Type', choices=[(b'I', b'Indivigual'), (b'G', b'Group')])),
                ('gender', models.CharField(default=b'M', max_length=2, verbose_name=b'Gender', choices=[(b'M', b'Male'), (b'F', b'Female')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MajorCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Major Category Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MinorCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Minor Category Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='majorCategory',
            field=models.ForeignKey(verbose_name=b'Major Category', to='nakshatrams.MajorCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='minorCategory',
            field=models.ForeignKey(verbose_name=b'Minor Category', to='nakshatrams.MinorCategory'),
            preserve_default=True,
        ),
    ]
