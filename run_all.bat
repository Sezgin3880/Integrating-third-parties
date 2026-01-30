@echo off
echo Running migrations...
python manage.py makemigrations
python manage.py migrate

echo Importing CSV data...
python manage.py import_csv

echo Starting server...
python manage.py runserver
