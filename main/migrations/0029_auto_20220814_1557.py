# Generated by Django 3.0 on 2022-08-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_networkpartner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkpartner',
            name='details',
            field=models.TextField(max_length=1000, verbose_name='Details'),
        ),
        migrations.AlterField(
            model_name='networkpartner',
            name='details_ar',
            field=models.TextField(max_length=1000, null=True, verbose_name='Details'),
        ),
        migrations.AlterField(
            model_name='networkpartner',
            name='details_en',
            field=models.TextField(max_length=1000, null=True, verbose_name='Details'),
        ),
    ]
