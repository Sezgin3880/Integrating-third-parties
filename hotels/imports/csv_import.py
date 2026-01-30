import csv
import requests
from io import StringIO
from django.conf import settings
from hotels.models import City, Hotel


def import_cities_from_url():
    # Haal CSV van internet
    r = requests.get(settings.CITY_CSV_URL, auth=(settings.CSV_USERNAME, settings.CSV_PASSWORD))
    r.raise_for_status()

    f = StringIO(r.text)
    reader = csv.reader(f, delimiter=';')

    for row in reader:
        code = row[0].replace('"', '').strip()
        name = row[1].replace('"', '').strip()

        # Voeg toe of update bestaande city
        City.objects.update_or_create(code=code, defaults={'name': name})


def import_hotels_from_url():
    # Haal hotel CSV
    r = requests.get(settings.HOTEL_CSV_URL, auth=(settings.CSV_USERNAME, settings.CSV_PASSWORD))
    r.raise_for_status()

    f = StringIO(r.text)
    reader = csv.reader(f, delimiter=';')

    for row in reader:
        city_code = row[0].replace('"', '').strip()
        hotel_code = row[1].replace('"', '').strip()
        name = row[2].replace('"', '').strip()

        # Zoek de bijbehorende city
        try:
            city = City.objects.get(code=city_code)
        except City.DoesNotExist:
            continue

        # Voeg hotel toe of update
        Hotel.objects.update_or_create(
            code=hotel_code,
            defaults={
                'name': name,
                'city': city
            }
        )
