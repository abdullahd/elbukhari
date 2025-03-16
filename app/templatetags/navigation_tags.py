from django import template
from wagtail.models import Page, Site

register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    # This returns a core.Page. The main menu needs to have the site.root_page
    # defined else will return an object attribute error ('str' object has no
    # attribute 'get_children')
    return Site.find_for_request(context['request']).root_page


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


def has_children(page):
    return page.get_children().live().exists()


def is_active(page, current_page):
    # To give us active state on main navigation
    return current_page.url_path.startswith(page.url_path) if current_page else False


@register.inclusion_tag('tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menu_items = parent.get_children().live().in_menu()

    for menu_item in menu_items:
        menu_item.show_dropdown = has_menu_children(menu_item)
        menu_item.active = (calling_page.url_path.startswith(menu_item.url_path)
                            if calling_page else False)
    return {
        'menu_items': menu_items,
        'request': context['request'],
        'calling_page': calling_page
    }

def external_link(page):
    try:
        return True if page.redirectpage.external_link else False
    except:
        return False

@register.inclusion_tag('tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent, calling_page=None):
    menu_items_children = parent.get_children().live().in_menu()
    for menu_item in menu_items_children:
        menu_item.has_dropdown = has_menu_children(menu_item)
        menu_item.active = (calling_page.url_path.startswith(menu_item.url_path)
                            if calling_page else False)
        menu_item.children = menu_item.get_children().live().in_menu()
        menu_item.external_link = external_link(menu_item)

    return {
        'menu_items_children': menu_items_children,
        'parent': parent,
        'request': context['request'],
    }


@register.inclusion_tag('tags/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self') or context.get('page') 
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(self, inclusive=True).filter(depth__gt=0)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }

