import logging

from django import template
from django.utils.translation import get_language

register = template.Library()
from django.template import loader

logger = logging.getLogger('django')


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()


@register.filter
def get_translation_data(object, field):
    """
        Get translated fields
    """
    language_code = get_language()
    field = field if language_code == 'en' else f'{language_code}_{field}'
    return getattr(object, f'{field}')


@register.simple_tag(takes_context=True)
def pagination(context):
    max_button_count = 5
    page_obj = context.get('page_obj', False)
    paginator = context.get('paginator', False)
    if paginator and page_obj:
        current_page = page_obj.number
        page_count = paginator.num_pages
        begin_page = max(1, current_page - (int)(max_button_count / 2))
        end_page = begin_page + max_button_count
        if end_page >= page_count:
            end_page = page_count + 1
            begin_page = max(1, end_page - max_button_count - 1)
        context.push({"page_range": range(begin_page, end_page)})
    context = {
        'page_obj': context.get('page_obj'),
        'request': context.get('request'),
        'page_range': context.get('page_range'),
        'paginator': context.get('paginator')
    }
    template = loader.get_template('main/partials/pagination.html')

    return template.render(context)
