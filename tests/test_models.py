from django.test import TestCase
from hotels.models import City, Hotel

class CityModelTest(TestCase):

    def test_city_creation(self):
        city = City.objects.create(code='AMS', name='Amsterdam')
        self.assertEqual(city.code, 'AMS')
        self.assertEqual(city.name, 'Amsterdam')


class HotelModelTest(TestCase):

    def test_hotel_belongs_to_city(self):
        city = City.objects.create(code='AMS', name='Amsterdam')
        hotel = Hotel.objects.create(
            code='AMS01',
            name='Ibis',
            city=city
        )

        self.assertEqual(hotel.city, city)
