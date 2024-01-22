from django.db import models

# Create your models here.

class continent(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 20)
    population = models.IntegerField()
    size = models.IntegerField()
    biggestcountry = models.CharField(max_length = 30)
    smallestcountry = models.CharField(max_length = 30)
    def __str__ (self):
        return self.name

class city(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 20)
    population = models.IntegerField()
    size = models.IntegerField()
    def __str__ (self):
        return self.name

class country(models.Model):
    id = models.BigAutoField(primary_key= True)
    name = models.CharField(max_length = 50)
    continent = models.ForeignKey(continent, on_delete = models.CASCADE)
    population = models.IntegerField()
    capital = models.ForeignKey(city, on_delete = models.CASCADE)
    GDP = models.IntegerField()
    age_made = models.IntegerField()
    def __str__ (self):
        return self.name