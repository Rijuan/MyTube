# Generated by Django 2.0.4 on 2018-05-24 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0025_auto_20180524_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='name_channel',
        ),
        migrations.RemoveField(
            model_name='video',
            name='uploader_name',
        ),
    ]