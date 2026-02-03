import csv
import requests
from io import StringIO
from django.conf import settings
from hotels.models import City, Hotel


def import_cities_from_url():
    # Fetch CSV from the internet
    r = requests.get(settings.CITY_CSV_URL, auth=(settings.CSV_USERNAME, settings.CSV_PASSWORD))
    r.raise_for_status()

    f = StringIO(r.text)
    reader = csv.reader(f, delimiter=';')

    for row in reader:
        code = row[0].replace('"', '').strip()
        name = row[1].replace('"', '').strip()

        # Add or update existing city
        City.objects.update_or_create(code=code, defaults={'name': name})


def import_hotels_from_url():
    # Fetch hotel CSV
    r = requests.get(settings.HOTEL_CSV_URL, auth=(settings.CSV_USERNAME, settings.CSV_PASSWORD))
    r.raise_for_status()

    f = StringIO(r.text)
    reader = csv.reader(f, delimiter=';')

    for row in reader:
        city_code = row[0].replace('"', '').strip()
        hotel_code = row[1].replace('"', '').strip()
        name = row[2].replace('"', '').strip()

        # Find the corresponding city
        try:
            city = City.objects.get(code=city_code)
        except City.DoesNotExist:
            continue

        # Add or update hotel
        Hotel.objects.update_or_create(
            code=hotel_code,
            defaults={
                'name': name,
                'city': city
            }
        )
