import csv
from hotels.models import City, Hotel

def import_cities(csv_path):
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            code, name = row
            city, created = City.objects.get_or_create(code=code, defaults={'name': name})
            if not created:
                city.name = name
                city.save()

def import_hotels(csv_path):
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            city_code, hotel_code, hotel_name = row
            try:
                city = City.objects.get(code=city_code)
            except City.DoesNotExist:
                continue  # sla hotels over waarvan de city nog niet bestaat
            hotel, created = Hotel.objects.get_or_create(
                code=hotel_code,
                defaults={'name': hotel_name, 'city': city}
            )
            if not created:
                hotel.name = hotel_name
                hotel.city = city
                hotel.save()
