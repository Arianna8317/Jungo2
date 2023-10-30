from django.core.management.base import BaseCommand
from app2.models import Product
class Command(BaseCommand):
    help = "Create Product."

    def handle(self, *args, **kwargs):
        product = Product(name='Blenamed', description='toothpaste', price=2.14, quantity=40)
        product.save()
        self.stdout.write(f'{product}')