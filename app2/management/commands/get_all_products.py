from django.core.management.base import BaseCommand
from app2.models import Product


class Command(BaseCommand):

    help = "Get all Products."
    
    def handle(self, *args, **kwargs):
        product = Product.objects.all()
        self.stdout.write(f'{product}')