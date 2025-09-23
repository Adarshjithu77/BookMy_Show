from django import forms
from .models import Movie, Show,Booking

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "description", "duration", "poster"]

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ["movie", "date", "time", "total_seats", "available_seats"]

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name", "seats_booked"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "border rounded p-2 w-full"}),
            "seats_booked": forms.NumberInput(attrs={"class": "border rounded p-2 w-full", "min":1}),}