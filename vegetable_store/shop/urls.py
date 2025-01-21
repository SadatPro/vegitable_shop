from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.vegetable_list, name='vegetable_list'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:vegetable_id>/', views.add_to_cart, name='add_to_cart'),
    path('order/create/', views.create_order, name='create_order'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
]
