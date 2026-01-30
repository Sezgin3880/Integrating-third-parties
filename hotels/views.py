from django.shortcuts import render
from hotels.models import City, Hotel

def hotels_by_city(request):
    cities = City.objects.all()
    selected_city = request.GET.get('city')
    hotels = []
    if selected_city:
        hotels = Hotel.objects.filter(city__code=selected_city)
    return render(request, 'hotels/hotels_by_city.html', {'cities': cities, 'hotels': hotels, 'selected_city': selected_city})
