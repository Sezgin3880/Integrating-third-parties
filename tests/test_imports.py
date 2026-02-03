import pytest
from unittest.mock import patch, MagicMock
from io import StringIO

from hotels.models import City, Hotel
from hotels.imports import import_cities_from_url, import_hotels_from_url

@pytest.mark.django_db
def test_import_cities_from_url():
    csv_content = '"C001";"Amsterdam"\n"C002";"Rotterdam"\n'
    
    mock_response = MagicMock()
    mock_response.text = csv_content
    mock_response.raise_for_status = MagicMock()

    with patch("requests.get", return_value=mock_response):
        import_cities_from_url()

    # Check cities are created
    amsterdam = City.objects.get(code="C001")
    rotterdam = City.objects.get(code="C002")
    assert amsterdam.name == "Amsterdam"
    assert rotterdam.name == "Rotterdam"


@pytest.mark.django_db
def test_import_hotels_from_url():
    # First, create cities
    city = City.objects.create(code="C001", name="Amsterdam")
    
    csv_content = '"C001";"H001";"Hotel Grand"\n"C001";"H002";"Hotel Central"\n'
    
    mock_response = MagicMock()
    mock_response.text = csv_content
    mock_response.raise_for_status = MagicMock()

    with patch("requests.get", return_value=mock_response):
        import_hotels_from_url()

    # Check hotels are created
    hotel1 = Hotel.objects.get(code="H001")
    hotel2 = Hotel.objects.get(code="H002")
    assert hotel1.name == "Hotel Grand"
    assert hotel1.city == city
    assert hotel2.name == "Hotel Central"
    assert hotel2.city == city


@pytest.mark.django_db
def test_import_hotels_skips_unknown_city():
    csv_content = '"UNKNOWN";"H003";"Hotel Unknown"\n'
    
    mock_response = MagicMock()
    mock_response.text = csv_content
    mock_response.raise_for_status = MagicMock()

    with patch("requests.get", return_value=mock_response):
        import_hotels_from_url()

    # No hotels should be created
    assert Hotel.objects.count() == 0
