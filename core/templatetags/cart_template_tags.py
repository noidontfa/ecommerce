from django import template
from core.models import Cart

register = template.Library()

@register.filter
def cart_item_count(user):

    if user.is_authenticated:
        cart = Cart.objects.filter(user_other=user)
        if cart.exists():
            return len(cart)
    return 0