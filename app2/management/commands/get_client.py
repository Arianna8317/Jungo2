from django.core.management.base import BaseCommand
from app2.models import Client
class Command(BaseCommand):
    help = "Get client by id."

    def add_arguments(self, parser):
        #parser.add_argument('id', type=int, help='Client ID')
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        #id = kwargs['id']
        pk = kwargs['pk']
        # client = Client.objects.get(id=id)
        client = Client.objects.filter(pk=pk).first()
        self.stdout.write(f'{client}')

