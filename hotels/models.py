from django.db import models

class City(models.Model):
    code = models.CharField(max_length=10, unique=True) #A short identifier like "NYC" or "LON"
    name = models.CharField(max_length=100) #Full name of the city like "New York City" or "London"

    def __str__(self):
        return f"{self.name} ({self.code})"

class Hotel(models.Model):
    code = models.CharField(max_length=20, unique=True) #A short identifier like "AMS01" or "ANT01"
    name = models.CharField(max_length=200) #Full name of the hotel like "Ibis Amsterdam Airport" or "Express by Holiday Inn"
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} in {self.city.code}"
