# Generated by Django 3.0 on 2022-08-13 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20220813_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
    ]
