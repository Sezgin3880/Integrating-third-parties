from django.core.management.base import BaseCommand
from hotels.imports.csv_import import import_cities, import_hotels

class Command(BaseCommand):
    help = 'Import cities and hotels from CSV files'

    def handle(self, *args, **options):
        import_cities('path/to/city.csv')
        import_hotels('path/to/hotel.csv')
        self.stdout.write(self.style.SUCCESS('Import finished'))
