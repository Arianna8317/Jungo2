from django.core.management.base import BaseCommand
from app2.models import Client
class Command(BaseCommand):
    help = "Update client name by id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('phone_number', type=str, help='Client phone number')
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        phone = kwargs.get('phone_number')
        client = Client.objects.filter(pk=pk).first()
        client.name = name
        client.phone_number = phone
        client.save()
        self.stdout.write(f'{client}')