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

## Setup

### 1. Installeer Django
```bash
python -m pip install django
```
### 2. Controleer INSTALLED_APPS
Zorg dat `hotels` in `INSTALLED_APPS` staat in `config/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'hotels',
]
```

### 3. Migreer de database

```bash
python manage.py makemigrations hotels
python manage.py migrate
```

### 4. Importeer CSV-data

Zorg ervoor dat `city.csv` en `hotel.csv` in de projectroot staan (naast `manage.py`).

Optie A - Via Django shell:

```bash
python manage.py shell
```

Vervolgens in de shell:

```python
from hotels.imports.csv_import import import_cities, import_hotels
import_cities('city.csv')
import_hotels('hotel.csv')
```

Optie B - Via management command (update eerst de paths in `hotels/commands/import_csv.py`):

```bash
python manage.py import_csv
```

### 5. Start de server

```bash
python manage.py runserver
```
## Gebruik

Open je browser en ga naar: **http://127.0.0.1:8000/hotels/**

Je ziet een dropdown met alle steden. Selecteer een stad en klik "Show hotels" om de hotels in die stad te bekijken.
