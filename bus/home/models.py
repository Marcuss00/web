from django.db import models

class BusSeat(models.Model):
    seat_number = models.IntegerField(unique=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.seat_number)


class Booking(models.Model):
    person_name = models.CharField(max_length=50)
    seat = models.OneToOneField(BusSeat, on_delete=models.CASCADE)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.person_name} - seat {self.seat.seat_number}"
