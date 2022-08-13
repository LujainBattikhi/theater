import logging

from django import template
from django.utils.translation import get_language

register = template.Library()

logger = logging.getLogger('django')


@register.filter
def get_translation_data(object, field):
    """
        Get translated fields
    """
    language_code = get_language()
    field = field if language_code == 'en' else f'{language_code}_{field}'
    return getattr(object, f'{field}')
