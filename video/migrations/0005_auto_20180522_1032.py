# Generated by Django 2.0.4 on 2018-05-22 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_auto_20180521_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='uname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]