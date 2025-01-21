from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vegetable, Cart, CartItem, Order
from django.contrib.auth.decorators import login_required
# Create your views here.

from vegetable_shop.models import Vegetable

def vegetable_list(request):
    vegetables = Vegetable.objects.all()
    return render(request, 'shop/vegetable_list.html', {'vegetables': vegetables})


@login_required
def add_to_cart(request, vegetable_id):
    vegetable = get_object_or_404(Vegetable, id=vegetable_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, vegetable=vegetable)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('shop:view_cart')
@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'shop/cart.html', {'cart': cart})
@login_required
def create_order(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    order = Order.objects.create(user=request.user, total_price=sum(item.vegetable.price * item.quantity for item in cart.items.all()))
    cart.items.all().delete()
    cart.delete()
    return redirect('shop:order_detail', order_id=order.id)
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'shop/order_detail.html', {'order': order})
