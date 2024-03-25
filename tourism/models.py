# lalibela_tourism/tourism/models.py

from django.db import models

class Tourist(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class TourPackage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Attraction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Booking(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)
    num_people = models.IntegerField()

    def __str__(self):
        return f"{self.tourist.name} - {self.tour_package.name}"
