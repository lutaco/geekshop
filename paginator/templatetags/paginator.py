from django import template
from django.core.paginator import Paginator
from paginator.settings import PAGINATION_PAGE_SIZE

register = template.Library()


@register.inclusion_tag('paginator/paginator.html', name='pagination', takes_context=True)
def render_paginator(context, value):

    if PAGINATION_PAGE_SIZE:
        request = context.get('request')
        page = request.GET.get('page')
        paginator = Paginator(value, PAGINATION_PAGE_SIZE)

        return {
            'page_obj': paginator.get_page(page),
            'paginator': paginator
        }


@register.filter(name='paginate')
def paginate(value, page):

    if PAGINATION_PAGE_SIZE:
        paginator = Paginator(value, PAGINATION_PAGE_SIZE)
        return paginator.get_page(page.get('page', 1))

    return value
