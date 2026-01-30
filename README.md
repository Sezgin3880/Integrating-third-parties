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

## Eén klik starten

Je kunt alles automatisch laten draaien met het bestand `run_all.bat`. Dit doet migraties uitvoeren, de CSV-data via HTTP importeren en de server starten. Dubbelklik op het bestand.