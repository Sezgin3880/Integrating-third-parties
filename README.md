# Integrating Third Parties

A Django project for integrating third-party services.

## Project Setup

This is a Django 6.0.1 project with a basic structure ready for integrating third-party APIs and services.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Sezgin3880/Integrating-third-parties.git
cd Integrating-third-parties
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Run the development server:
```bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000/

## Project Structure

- `integrating_third_parties/` - Main project configuration
- `core/` - Core application for base functionality
- `manage.py` - Django management script
- `requirements.txt` - Python dependencies

## Development

- Check for issues: `python manage.py check`
- Run tests: `python manage.py test`
- Create superuser: `python manage.py createsuperuser`

## License

See LICENSE file for details.
