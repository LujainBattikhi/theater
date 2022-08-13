# Register your models here.
from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE

from main.models import Category, SubCategory, Production, TeamMember, HeadLine

admin.site.register(Category)
admin.site.register(Production)
admin.site.register(SubCategory)
admin.site.register(TeamMember)


class textEditorAdmin(admin.ModelAdmin):
    list_display = ["title"]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(HeadLine, textEditorAdmin)
