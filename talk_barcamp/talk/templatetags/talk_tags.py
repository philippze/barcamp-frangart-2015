from django import template

from cms.models import Page


register = template.Library()


@register.assignment_tag(takes_context=True)
def get_next_page(context):
    current_page = context['request'].current_page
    return current_page.get_next_filtered_sibling(publisher_is_draft=False)

@register.assignment_tag(takes_context=True)
def get_prev_page(context):
    current_page = context['request'].current_page
    return current_page.get_previous_filtered_sibling(publisher_is_draft=False)
