from django import template
from menu.models import MenuItem

register = template.Library()

@register.inclusion_tag(filename='menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(title=menu_name)
    
    active_url = context.request.path

    def render_menu(items):
        result = []
        for item in items:
            children = item.children.all()
            result.append({
                'item': item,
                'children': render_menu(children) if item.title == menu_name or item.url in active_url else None,
            })
        return result

    menu = render_menu(menu_items)

    return {
        'menu': menu,
    }
