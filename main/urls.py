"""theater URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from main.views import Main, ProductionListView, ProductionDetails, TeamList, TeamMemberDetails, HeadLineDetailView, \
    AnnualReportsDetailView, NetworkPartnerDetailView, DonateSupportTemplateView, ContactUsTemplateView

app_name = 'main'

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('category/<str:slug>', ProductionListView.as_view(), name='sub_category_details'),
    path('category/', ProductionListView.as_view(), name='sub_category_details'),
    path('production/<str:slug>', ProductionDetails.as_view(), name='production_details'),
    path('team', TeamList.as_view(), name='team'),
    path('team/<str:slug>', TeamMemberDetails.as_view(), name='team_member'),
    path('headline/<str:slug>', HeadLineDetailView.as_view(), name='headline'),
    path('annual-reports', AnnualReportsDetailView.as_view(), name='annual_reports'),
    path('networks-&-partners', NetworkPartnerDetailView.as_view(), name='networks_and_partners'),
    path('donate-&-support', DonateSupportTemplateView.as_view(), name='donate_and_support'),
    path('contact-us', ContactUsTemplateView.as_view(), name='contact_us'),
]
