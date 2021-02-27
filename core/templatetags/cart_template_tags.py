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

@register.filter
def get_price_cart(user):

    total_price = 0
    if user.is_authenticated:
        cart = Cart.objects.filter(user_other=user)
        if cart.exists():
            for item in cart:
                total_price += item.product.price * item.quantity
    return total_price