from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.PositiveIntegerField(default=90)
    poster = models.ImageField(upload_to="posters/", blank=True, null=True)

    def _str_(self):
        return self.title

class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    total_seats = models.PositiveIntegerField(default=50)
    available_seats = models.PositiveIntegerField(default=50)

class Booking(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    seats_booked = models.PositiveIntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.name} - {self.show.movie.title} ({self.seats_booked} seats)"