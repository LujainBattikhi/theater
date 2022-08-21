from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
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
        verbose_name=_('Embed Youtube Link'),
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
    partners_image = models.ImageField(
        null=True,
        blank=True,
        verbose_name=_("Partners Photo"),
        upload_to='partners'
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
        return 'synopsis', 'title',

    def __str__(self):
        return self.title


class ProductionEvent(BaseModel):
    """
    Production Event model
    """
    date = models.DateField(
        blank=False, null=False,
        verbose_name=_('Date'),
    )
    time = models.TimeField(
        blank=False, null=False,
        verbose_name=_('Time'),
    )
    place = models.CharField(
        max_length=150,
        blank=False, null=False,
        verbose_name=_('Place'),
    )
    title = models.CharField(
        max_length=150,
        blank=False, null=False,
        verbose_name=_('Title'),
    )
    production = models.ForeignKey(
        Production, null=False,
        related_name='events', on_delete=models.PROTECT,
    )

    class Meta:
        ordering = ['date', ]

    @staticmethod
    def translatable_fields_list():
        return 'place', 'title'


class ProductionImage(models.Model):
    TYPE_GALLERY = 'gallery'
    TYPE_NEWS = 'news'
    TYPE_CHOICES = [
        (TYPE_GALLERY, _('Gallery')),
        (TYPE_NEWS, _('News')),
    ]
    production = models.ForeignKey(Production, related_name='images', on_delete=models.PROTECT, )
    image = models.ImageField()
    type = models.CharField(
        default=TYPE_GALLERY, max_length=255,
        choices=TYPE_CHOICES,
        verbose_name=_('Type')
    )


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


class TeamMemberSocialMedia(models.Model):
    TYPE_FACEBOOK = 'facebook'
    TYPE_TWITTER = 'twitter'
    TYPE_YOUTUBE = 'youtube'
    TYPE_INSTAGRAM = 'instagram'
    TYPE_WEBSITE = 'website'
    TYPE_CHOICES = [
        (TYPE_FACEBOOK, _('Facebook')),
        (TYPE_TWITTER, _('Twitter')),
        (TYPE_YOUTUBE, _('Youtube')),
        (TYPE_INSTAGRAM, _('Instagram')),
        (TYPE_WEBSITE, _('Website')),
    ]
    team_member = models.ForeignKey(TeamMember, related_name='social_media_links', on_delete=models.PROTECT, )
    link = models.URLField()
    type = models.CharField(
        blank=True, null=False,
        max_length=255,
        choices=TYPE_CHOICES,
        verbose_name=_('Type')
    )


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
