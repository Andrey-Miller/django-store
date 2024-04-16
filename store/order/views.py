from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import User, Order

def fetch_user_orders(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(user=user)
    context = {
        'user': user,
        'orders': orders,
    }
    return render(request, 'orders/orders.html', context)

def fetch_ordered_products(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    year_ago = today - timedelta(days=365)

    orders_week = Order.objects.filter(user=user, order_date__gte=week_ago)
    orders_month = Order.objects.filter(user=user, order_date__gte=month_ago)
    orders_year = Order.objects.filter(user=user, order_date__gte=year_ago)

    products_week = set()
    products_month = set()
    products_year = set()

    for order in orders_week:
        products_week.update(order.products.all())

    for order in orders_month:
        products_month.update(order.products.all())

    for order in orders_year:
        products_year.update(order.products.all())

    context = {
        'user': user,
        'products_week': products_week,
        'products_month': products_month,
        'products_year': products_year,
    }

    return render(request, 'orders/ordered_products_sort.html', context)