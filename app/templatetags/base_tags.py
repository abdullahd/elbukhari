from django import template
import re
import json
from wagtail.models import Page
from django.db.models.functions import Upper

register=template.Library()


def header_footer_content():
    from app.models import SiteHeaderFooter
    obj = SiteHeaderFooter.objects.all().first()
    return obj.header_footer_content.raw_data if obj else None


@register.inclusion_tag('tags/policy_links.html')
def policy_links_section():
    content = header_footer_content()
    if content:
        for block in content:
            if block['type'] == 'policy_block':
                return {
                    'links': block['value']
                }
    return None


@register.inclusion_tag('tags/social_media.html')
def social_media_section():
    content = header_footer_content()

    if content:
        for block in content:
            if block['type'] == 'social_media_block':
                return {
                    'links': block['value']
                }        
    return None
