# Generated by Django 3.0 on 2022-08-19 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220819_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Updated At')),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('place', models.CharField(max_length=150, verbose_name='Place')),
                ('place_en', models.CharField(max_length=150, null=True, verbose_name='Place')),
                ('place_ar', models.CharField(max_length=150, null=True, verbose_name='Place')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Title')),
                ('title_ar', models.CharField(max_length=150, null=True, verbose_name='Title')),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schedules', to='main.Production')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='ProductionSchedule',
        ),
    ]
