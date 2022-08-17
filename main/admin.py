# Register your models here.

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from main.models import Category, SubCategory, Production, TeamMember, HeadLine, AnnualReport, NetworkPartner, \
    ProductionImage

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(TeamMember)
admin.site.register(AnnualReport)
admin.site.register(NetworkPartner)


class ProductionImageInline(admin.TabularInline):
    model = ProductionImage
    extra = 3
    max_num = 20


class ProductionAdmin(admin.ModelAdmin):
    inlines = [ProductionImageInline, ]


admin.site.register(Production, ProductionAdmin)


class HeadLineAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = HeadLine
        fields = '__all__'


class HeadLineAdmin(admin.ModelAdmin):
    form = HeadLineAdminForm


admin.site.register(HeadLine, HeadLineAdmin)
