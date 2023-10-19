from django.core.management.base import BaseCommand
from app2.models import Client
class Command(BaseCommand):
    help = "Create client."
    def handle(self, *args, **kwargs):
        client = Client(name='Serg', email='serg@example.com', address='Chicago', phone_number="165544556")
        client.save()
        self.stdout.write(f'{client}')