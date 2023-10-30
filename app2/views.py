# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Client, Order, Product, OrderProducts
from django.http import HttpResponse
from datetime import datetime, timedelta
# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")


def about(request):
    return HttpResponse("This is the about page.")


def client_orders(request, client_id):
    client= get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer=client)
    return render(request, "app2/client_orders.html", {'client': client, 'orders': orders})

def client_orders_filtered(request, client_id, days_ago):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(date_ordered__gt=datetime.now()-timedelta(days=days_ago))
    orders = orders.filter(customer=client_id)
    return render(request, "app2/client_orders.html", {'client': client, 'orders': orders})

def order_view(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    orderproducts = OrderProducts.objects.filter(order=order)
    return render(request, "app2/order_view.html", {'order': order, 'orderproducts': orderproducts})


