# Generated by Django 3.0 on 2022-08-14 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_annualreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Updated At')),
                ('name', models.CharField(max_length=150, verbose_name='Title')),
                ('name_en', models.CharField(max_length=150, null=True, verbose_name='Title')),
                ('name_ar', models.CharField(max_length=150, null=True, verbose_name='Title')),
                ('details', models.TextField(max_length=500, verbose_name='Details')),
                ('details_en', models.TextField(max_length=500, null=True, verbose_name='Details')),
                ('details_ar', models.TextField(max_length=500, null=True, verbose_name='Details')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
