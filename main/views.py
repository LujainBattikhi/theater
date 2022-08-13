from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from main.models import SubCategory, Production, TeamMember


class Main(TemplateView):
    template_name = 'main/main.html'


class SubCategoryDetails(DetailView):
    template_name = 'main/sub_category.html'
    model = SubCategory


class ProductionDetails(DetailView):
    template_name = 'main/production.html'
    model = Production


class TeamList(ListView):
    template_name = 'main/team.html'
    model = TeamMember
    paginate_by = 10


class TeamMemberDetails(DetailView):
    template_name = 'main/team_member.html'
    model = TeamMember
