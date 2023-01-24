from django.db import models

# Create your models here.

class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_Guests = models.PositiveSmallIntegerField()
    BookingDate = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.Name


class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.Title
