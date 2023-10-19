from django.core.management.base import BaseCommand
from app2.models import Product
class Command(BaseCommand):
    help = "Create Product."

    def handle(self, *args, **kwargs):
        product = Product(name='Shauma', description='Shampoo', price=45.14, quantity=15)
        product.save()
        self.stdout.write(f'{product}')