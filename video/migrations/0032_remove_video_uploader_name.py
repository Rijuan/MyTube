# Generated by Django 2.0.4 on 2018-05-25 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0031_auto_20180525_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='Uploader_name',
        ),
    ]
