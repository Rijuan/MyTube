# Generated by Django 2.0.4 on 2018-05-24 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0022_auto_20180524_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
