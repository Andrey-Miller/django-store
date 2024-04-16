from django.urls import path

from order.views import fetch_user_orders, fetch_ordered_products

urlpatterns = [
    path('user-orders/<int:user_id>', fetch_user_orders, name='user_orders'),
    path('ordered-products/<int:user_id>', fetch_ordered_products,
         name='ordered_products'),
]