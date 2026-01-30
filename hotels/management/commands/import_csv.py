from django.core.management.base import BaseCommand
from hotels.imports.csv_import import (
    import_cities_from_url,
    import_hotels_from_url
)


class Command(BaseCommand):
    help = 'Import cities and hotels from remote CSV files'

    def handle(self, *args, **options):
        self.stdout.write('Importing cities...')
        import_cities_from_url()

        self.stdout.write('Importing hotels...')
        import_hotels_from_url()

        self.stdout.write(self.style.SUCCESS('Import finished'))
