# Generated by Django 3.0 on 2022-08-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_production_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='image',
            field=models.ImageField(default=1, upload_to='covers', verbose_name='Cover Photo'),
            preserve_default=False,
        ),
    ]
