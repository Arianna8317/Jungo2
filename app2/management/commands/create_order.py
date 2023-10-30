from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from app2.models import Product, Order, OrderProducts, Client
class Command(BaseCommand):
    help = "Create Order."

    def handle(self, *args, **kwargs):
        order = Order.objects.create(customer=Client.objects.get(name="Serg"), total_price=0)
        order.date_ordered -= timedelta(days=262)
        product1 = Product.objects.get(name="Blendamed")
        orderproduct1 = OrderProducts(order=order, product=product1, quantity=3)
        orderproduct1.save()
        order.products.add(product1)
        order.total_price += product1.price*orderproduct1.quantity
        product2 = Product.objects.get(name="Saveguard")
        orderproduct2 = OrderProducts(order=order, product=product2, quantity=2)
        orderproduct2.save()
        order.products.add(product2)
        order.total_price += product2.price*orderproduct2.quantity
        order.save()
        self.stdout.write(f'{order}')

