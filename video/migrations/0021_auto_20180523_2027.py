# Generated by Django 2.0.4 on 2018-05-23 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0020_auto_20180523_2022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='channel_name',
            new_name='name_channel',
        ),
    ]