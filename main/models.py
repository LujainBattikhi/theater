from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


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
        return reverse("sub_category_details", kwargs={"slug": self.slug})

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
    synopsis = models.TextField(
        max_length=5000,
        blank=False, null=False,
        verbose_name=_('Synopsis'),
    )
    link = models.URLField(
        verbose_name=_('Link'),
    )

    @staticmethod
    def translatable_fields_list():
        return 'title', 'synopsis',

    def __str__(self):
        return self.title
