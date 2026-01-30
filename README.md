# Integrating Third Parties - Django Hotel Import

## Overzicht
Een klein Django-project dat hotel- en city-data uit CSV-bestanden importeert en per stad toont in een eenvoudige frontend.

- **City**: code + naam  
- **Hotel**: code, naam, gekoppeld aan een city  

Project bevat:
- Django modellen (`City`, `Hotel`)  
- CSV-import functies  
- Een simpele view + template om hotels per stad te tonen  

---

## Structuur

Integrating-third-parties/
├── config/ # Django settings
├── hotels/ # App
│ ├── imports/ # CSV import logic
│ ├── templates/
│ │ └── hotels/ # Views templates
│ ├── urls.py
│ ├── views.py
│ ├── models.py
│ └── tests/
├── city.csv
├── hotel.csv
├── manage.py
└── README.md


---

## Setup

1. Installeer Django:

```bash
python -m pip install django
Zorg dat hotels in INSTALLED_APPS staat (config/settings.py):

INSTALLED_APPS = [
    ...
    'hotels',
]
Migrate database:

python manage.py makemigrations hotels
python manage.py migrate
Importeer CSV-data:

python manage.py shell
from hotels.imports.csv_import import import_cities, import_hotels
import_cities('city.csv')
import_hotels('hotel.csv')
Optioneel via management command:

python manage.py import_csv
Runnen
python manage.py runserver
Open browser: http://127.0.0.1:8000/hotels/
Selecteer een stad om hotels te bekijken.
