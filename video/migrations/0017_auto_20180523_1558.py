# Generated by Django 2.0.4 on 2018-05-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0016_auto_20180523_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
    ]