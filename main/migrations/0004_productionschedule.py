# Generated by Django 3.0 on 2022-08-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220819_0211'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Updated At')),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('place', models.TextField(verbose_name='Time')),
                ('place_en', models.TextField(null=True, verbose_name='Time')),
                ('place_ar', models.TextField(null=True, verbose_name='Time')),
                ('title', models.TextField(verbose_name='Time')),
                ('title_en', models.TextField(null=True, verbose_name='Time')),
                ('title_ar', models.TextField(null=True, verbose_name='Time')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
