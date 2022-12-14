# Generated by Django 3.0 on 2022-08-15 14:55

import autoslug.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Updated At')),
                ('publish_date', models.DateField(blank=True, db_index=True, null=True, verbose_name='Publish At')),
                ('pdf', models.FileField(upload_to='annual_reports', verbose_name='PDF')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Updated At')),
                ('name', models.CharField(db_index=True, max_length=80, verbose_name='Name')),
                ('name_en', models.CharField(db_index=True, max_length=80, null=True, verbose_name='Name')),
                ('name_ar', models.CharField(db_index=True, max_length=80, null=True, verbose_name='Name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HeadLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Updated At')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Title')),
                ('title_ar', models.CharField(max_length=150, null=True, verbose_name='Title')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('content_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('content_ar', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=['title', 'created_at'])),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NetworkPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Updated At')),
                ('name', models.CharField(max_length=150, verbose_name='Title')),
                ('name_en', models.CharField(max_length=150, null=True, verbose_name='Title')),
                ('name_ar', models.CharField(max_length=150, null=True, verbose_name='Title')),
                ('details', models.TextField(max_length=1000, verbose_name='Details')),
                ('details_en', models.TextField(max_length=1000, null=True, verbose_name='Details')),
                ('details_ar', models.TextField(max_length=1000, null=True, verbose_name='Details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Updated At')),
                ('name', models.CharField(max_length=150, verbose_name='Full Name')),
                ('name_en', models.CharField(max_length=150, null=True, verbose_name='Full Name')),
                ('name_ar', models.CharField(max_length=150, null=True, verbose_name='Full Name')),
                ('job_title', models.CharField(max_length=150, verbose_name='Job Title')),
                ('job_title_en', models.CharField(max_length=150, null=True, verbose_name='Job Title')),
                ('job_title_ar', models.CharField(max_length=150, null=True, verbose_name='Job Title')),
                ('image', models.ImageField(upload_to='covers', verbose_name='Personal Photo')),
                ('bio', models.TextField(blank=True, max_length=5000, verbose_name='Bio')),
                ('bio_en', models.TextField(blank=True, max_length=5000, null=True, verbose_name='Bio')),
                ('bio_ar', models.TextField(blank=True, max_length=5000, null=True, verbose_name='Bio')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=['name', 'created_at'])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Updated At')),
                ('name', models.CharField(db_index=True, max_length=80, verbose_name='Name')),
                ('name_en', models.CharField(db_index=True, max_length=80, null=True, verbose_name='Name')),
                ('name_ar', models.CharField(db_index=True, max_length=80, null=True, verbose_name='Name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=['name', 'created_at'])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sub_categories', to='main.Category', verbose_name='Sub Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Updated At')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Title')),
                ('title_ar', models.CharField(max_length=150, null=True, verbose_name='Title')),
                ('synopsis', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Synopsis')),
                ('synopsis_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Synopsis')),
                ('synopsis_ar', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Synopsis')),
                ('link', models.URLField(verbose_name='Link')),
                ('publish_date', models.DateField(blank=True, db_index=True, null=True, verbose_name='Publish At')),
                ('image', models.ImageField(upload_to='covers', verbose_name='Cover Photo')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=['title', 'created_at'])),
                ('is_featured', models.BooleanField(default=False)),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='productions', to='main.SubCategory', verbose_name='Sub Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
