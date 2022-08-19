from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, FormView, ListView
from django.views.generic.detail import DetailView

from main.forms import MessageForm
from main.models import Production, TeamMember, HeadLine, AnnualReport, NetworkPartner, SubCategory, ProductionImage, \
    ProductionEvent
from main.utils import send_email


class Main(TemplateView):
    template_name = 'main/main.html'

    def get_context_data(self, **kwargs):
        context = super(Main, self).get_context_data(**kwargs)
        context['featured_productions'] = Production.objects.filter(is_featured=True)[:6]
        return context


class ProductionListView(ListView):
    template_name = 'main/sub_category.html'
    model = Production
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug', None)
        self.object = SubCategory.objects.filter(slug=slug).first()
        if slug and not self.object:
            messages.error(request,
                           _("Sorry!"),
                           extra_tags=_("Category Not Found!"))
            return redirect(reverse('main:main'))
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        slug = self.kwargs.get('slug', None)
        if not slug:
            object_list = super().get_queryset()
        else:
            object_list = self.object.productions
        search = self.request.GET.get('search', '')
        queryset = object_list.filter(
            Q(title__icontains=search) |
            Q(synopsis__icontains=search) |
            Q(sub_category__name__icontains=search)

        )
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductionListView, self).get_context_data(**kwargs)
        context['object'] = self.object
        return context


class ProductionDetails(DetailView):
    template_name = 'main/production.html'
    model = Production

    def get_context_data(self, **kwargs):
        context = super(ProductionDetails, self).get_context_data(**kwargs)
        context['gallery'] = self.object.images.filter(type=ProductionImage.TYPE_GALLERY)
        context['news'] = self.object.images.filter(type=ProductionImage.TYPE_NEWS)
        return context


class ProductionEventListView(ListView):
    template_name = 'main/production_event.html'
    model = ProductionEvent

    def dispatch(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug', None)
        object_list = super().get_queryset()
        self.available_dates = object_list.values_list('date', flat=True).distinct()
        self.date = self.request.GET.get('date', None) or self.available_dates.first()
        self.object_list = object_list.filter(production__slug=slug, date=self.date).distinct()
        if not self.object_list:
            return redirect(reverse('main:main'))
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductionEventListView, self).get_context_data(**kwargs)
        context['production'] = self.object_list.first().production
        context['available_dates'] = self.available_dates
        context['active_date'] = self.date
        context['hide_coming_soon'] = True
        context['show_languages'] = True
        return context


class TeamList(ListView):
    template_name = 'main/team.html'
    model = TeamMember
    paginate_by = 10


class TeamMemberDetails(DetailView):
    template_name = 'main/team_member.html'
    model = TeamMember


class HeadLineDetailView(DetailView):
    template_name = 'main/head_line.html'
    model = HeadLine


class AnnualReportsDetailView(ListView):
    template_name = 'main/annual_reports.html'
    model = AnnualReport
    paginate_by = 10


class NetworkPartnerDetailView(ListView):
    template_name = 'main/networks_partners.html'
    model = NetworkPartner
    paginate_by = 10


class DonateSupportTemplateView(TemplateView):
    template_name = 'main/donate_and_support.html'


class ContactUsTemplateView(FormView):
    template_name = 'main/contact_us.html'
    form_class = MessageForm
    success_url = reverse_lazy('main:main')

    def form_valid(self, form):
        data = form.cleaned_data
        to_email = data.get('email')
        send_email(
            subject=data.get('subject'),
            template_name='main/emails/contact_us.html',
            context={
                'name': data.get('name'),
                'email': to_email,
                'body': data.get('body'),
            },
            to_emails=[settings.DEFAULT_EMAIL],
            from_email=[to_email],
        )

        send_email(
            subject=_('Thank you for contacting us'),
            template_name='main/emails/thank_you.html',
            context={
                'name': data.get('name'),
            },
            to_emails=[to_email],
            from_email=settings.DEFAULT_EMAIL,
        )

        messages.add_message(
            request=self.request, level=messages.SUCCESS,
            message=_('Message has been sent successfully!')
        )
        return redirect(self.get_success_url())
