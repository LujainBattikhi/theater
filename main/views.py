from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from main.models import SubCategory


class Main(TemplateView):
    template_name = 'main/main.html'


class SubCategoryDetails(DetailView):
    template_name = 'main/sub_category.html'
    model = SubCategory
