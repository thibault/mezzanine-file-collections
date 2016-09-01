# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('file', mezzanine.core.fields.FileField(max_length=200, verbose_name='File')),
                ('title', models.CharField(max_length=50, verbose_name='Title', blank=True)),
                ('description', models.CharField(max_length=1000, verbose_name='Description', blank=True)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Media File',
                'verbose_name_plural': 'Media Files',
            },
        ),
        migrations.CreateModel(
            name='MediaLibrary',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Media Library',
                'verbose_name_plural': 'Media Libraries',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='library',
            field=models.ForeignKey(related_name='files', to='mezzanine_file_collections.MediaLibrary'),
        ),
    ]
