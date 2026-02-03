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

### Vereisten
- Python 3.11 of 3.12
- pip

### Installatie

```bash
# 1. Clone the repository
git clone <repo-url>
cd Integrating-third-parties

# 2. Install dependencies
pip install -r requirements.txt

# 3. Database migration
python manage.py migrate

# 4. Start the development server
python manage.py runserver