from django.db import models

# Create your models here.

times = (
    ("12:00", "12:00"),
    ("12:30", "12:30"),
    ("01:00", "01:00"),
    ("01:30", "01:30"),
    ("02:00", "02:00"),
    ("02:30", "02:30"),
    ("03:00", "03:00"),
    ("18:00", "18:00"),
    ("18:30", "18:30"),
    ("19:00", "19:00"),
    ("20:30", "20:30"),
    ("21:00", "21:00"),
    )

guest_choices = (
    (1, "1 person"),
    (2, "2 person"),
    (3, "3 person"),
    (4, "4 person"),
    (5, "5 person"),
    (6, "6 person"),
    (7, "7 person"),
    )

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    number_of_guests = models.IntegerField(choices= guest_choices, default= 1 )
    requested_date = models.DateField()
    requested_time = models.TimeField()

    def __str__(self):
        return self.name
   