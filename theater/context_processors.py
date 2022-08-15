import logging

from main.models import Category, HeadLine

logger = logging.getLogger('default')
from django.conf import settings


def get_navbar_details(request):
    """
    :param request:
    :return:
    """
    categories = Category.objects.filter(is_active=True)
    head_lines = HeadLine.objects.filter(is_active=True)
    return {'categories': categories, 'headlines': head_lines, 'host': settings.HOST}
