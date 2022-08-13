# Register your models here.
from django.contrib import admin

from main.models import Category, SubCategory, Production

admin.site.register(Category)
admin.site.register(Production)
admin.site.register(SubCategory)
