from django.shortcuts import render
from .forms import CitySelectForm
from hotels.models import City, Hotel

def hotels_view(request):
    cities = City.objects.all()
    selected_city = request.GET.get('city')

    # Form init with cities
    form = CitySelectForm(request.GET or None, cities=cities)

    # hotels filtered by selected city
    hotels = Hotel.objects.filter(city__code=selected_city) if selected_city else []

    return render(request, 'hotel.html', {
        'form': form,
        'hotels': hotels,
        'selected_city': selected_city,
        'cities': cities,
    })
