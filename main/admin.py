# Register your models here.

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from main.models import Category, SubCategory, Production, TeamMember, HeadLine, AnnualReport, NetworkPartner

admin.site.register(Category)
admin.site.register(Production)
admin.site.register(SubCategory)
admin.site.register(TeamMember)
admin.site.register(AnnualReport)
admin.site.register(NetworkPartner)


class HeadLineAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = HeadLine
        fields = '__all__'


class HeadLineAdmin(admin.ModelAdmin):
    form = HeadLineAdminForm


admin.site.register(HeadLine, HeadLineAdmin)
