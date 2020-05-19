from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Ensures that teh cart contents are available when rendering every page
    """

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    points = 0
    product_count = 0

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        points += quantity * product.points
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})

    return {'cart_items': cart_items,
            'total': total,
            'points': points,
            'product_count': product_count}
