from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.

class BaseModel(models.Model):
    """
    Base parent model for all the models
    """
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True, verbose_name=_('Created At'), db_index=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True, verbose_name=_('Updated At'), db_index=True
    )

    class Meta:
        abstract = True


class Category(BaseModel):
    """
    Category model
    """
    name = models.CharField(
        max_length=80,
        blank=False, null=False,
        verbose_name=_('Name'),
        db_index=True
    )
    is_active = models.BooleanField(
        verbose_name=_('Is Active'),
        default=True
    )

    @staticmethod
    def translatable_fields_list():
        return 'name',

    def __str__(self):
        return self.name


class SubCategory(BaseModel):
    """
    Sub Category model
    """
    name = models.CharField(
        max_length=80,
        blank=False, null=False,
        verbose_name=_('Name'),
        db_index=True
    )
    category = models.ForeignKey(
        Category,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name=_("Sub Category"),
        related_name='sub_categories'
    )
    is_active = models.BooleanField(
        verbose_name=_('Is Active'),
        default=True
    )
    slug = AutoSlugField(
        populate_from='name',
        unique_with=['name', 'created_at'],
    )

    def get_absolute_url(self):
        return reverse("main:sub_category_details", kwargs={"slug": self.slug})

    @staticmethod
    def translatable_fields_list():
        return 'name',

    def __str__(self):
        return self.name


class Production(BaseModel):
    """
    Production model
    """
    title = models.CharField(
        max_length=150,
        blank=False, null=False,
        verbose_name=_('Title'),
    )
    synopsis = RichTextUploadingField(
        blank=False, null=False,
        verbose_name=_('Synopsis'),
    )
    sub_category = models.ForeignKey(
        SubCategory,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name=_("Sub Category"),
        related_name='productions'
    )
    link = models.URLField(
        verbose_name=_('Link'),
    )
    publish_date = models.DateField(
        blank=True, null=True, verbose_name=_('Publish At'), db_index=True
    )
    image = models.ImageField(
        null=False,
        blank=False,
        verbose_name=_("Cover Photo"),
        upload_to='covers'
    )

    slug = AutoSlugField(
        populate_from='title',
        unique_with=['title', 'created_at'],
    )
    is_featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("main:production_details", kwargs={"slug": self.slug})

    @staticmethod
    def translatable_fields_list():
        return 'title', 'synopsis',

    def __str__(self):
        return self.title


class TeamMember(BaseModel):
    """
    Production model
    """
    name = models.CharField(
        max_length=150,
        blank=False, null=False,
        verbose_name=_('Full Name'),
    )
    job_title = models.CharField(
        max_length=150,
        blank=False, null=False,
        verbose_name=_('Job Title'),
    )
    image = models.ImageField(
        null=False,
        blank=False,
        verbose_name=_("Personal Photo"),
        upload_to='covers'
    )
    bio = models.TextField(
        max_length=5000,
        blank=True, null=False,
        verbose_name=_('Bio'),
    )
    slug = AutoSlugField(
        populate_from='name',
        unique_with=['name', 'created_at'],
    )

    def get_absolute_url(self):
        return reverse("main:team_member", kwargs={"slug": self.slug})

    @staticmethod
    def translatable_fields_list():
        return 'name', 'job_title', 'bio',

    def __str__(self):
        return self.name


class HeadLine(BaseModel):
    """
    HeadLine model
    """
    title = models.CharField(
        max_length=150,
        blank=False, null=False,
        verbose_name=_('Title'),
    )
    content = RichTextUploadingField()

    slug = AutoSlugField(
        populate_from='title',
        unique_with=['title', 'created_at'],
    )

    is_active = models.BooleanField(
        verbose_name=_('Is Active'),
        default=True
    )

    def get_absolute_url(self):
        return reverse("main:headline", kwargs={"slug": self.slug})

    @staticmethod
    def translatable_fields_list():
        return 'title', 'content',

    def __str__(self):
        return self.title


class AnnualReport(BaseModel):
    """
    Annual Reports model
    """
    publish_date = models.DateField(
        blank=True, null=True,
        verbose_name=_('Publish At'), db_index=True
    )
    pdf = models.FileField(
        null=False,
        blank=False,
        verbose_name=_("PDF"),
        upload_to='annual_reports'
    )

    def __str__(self):
        return f'{self.publish_date}'


class NetworkPartner(BaseModel):
    """
    Annual Reports model
    """
    name = models.CharField(
        max_length=150,
        blank=False, null=False,
        verbose_name=_('Title'),
    )
    details = models.TextField(
        max_length=1000,
        blank=False, null=False,
        verbose_name=_('Details'),
    )

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def translatable_fields_list():
        return 'name', 'details',
