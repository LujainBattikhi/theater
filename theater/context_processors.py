import logging

from main.models import Category

logger = logging.getLogger('default')


def get_navbar_details(request):
    """
    :param request:
    :return:
    """
    categories = Category.objects.filter(is_active=True)
    return {'categories': categories}
