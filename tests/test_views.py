from django.test import TestCase
from hotels.models import City, Hotel

class HotelViewTest(TestCase):

# Test that the hotels page loads successfully (HTPP 200)
    def test_hotels_page_loads(self):
        response = self.client.get('/hotels/')
        self.assertEqual(response.status_code, 200)

# Test that filtering hotels by city shows only hotels in that city
    def test_hotels_filtered_by_city(self):
        city = City.objects.create(code='AMS', name='Amsterdam')
        Hotel.objects.create(code='AMS01', name='Ibis', city=city)

        response = self.client.get('/hotels/', {'city': 'AMS'})

        self.assertContains(response, 'Ibis')
