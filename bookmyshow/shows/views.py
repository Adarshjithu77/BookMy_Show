from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Movie, Show
from .forms import MovieForm, ShowForm,BookingForm

def home(request):
    movies = Movie.objects.all()
    movie_data = []

    for movie in movies:
        shows = Show.objects.filter(movie=movie)
        movie_data.append({
            "movie": movie,
            "shows": shows
        })

    return render(request, "home.html", {"movies":movies})

def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MovieForm()
    return render(request, "add_movie.html", {"form": form})

def add_show(request):
    if request.method == "POST":
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ShowForm()
    return render(request, "add_show.html", {"form": form})

def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return HttpResponse("<h1>Movie not found</h1>", status=404)
    shows = Show.objects.filter(movie=movie)
    return render(request, "movie_detail.html", {'movie': movie, 'shows': shows})

def book_ticket(request, show_id):
    try:
        show = Show.objects.get(id=show_id)
    except Show.DoesNotExist:
        return HttpResponse("<h1>Show not found</h1>", status=404)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if booking.seats_booked > show.available_seats:
                return render(request, "book_ticket.html", {
                    "show": show,
                    "form": form,
                    "error": "Not enough seats available."
                })
            
            show.available_seats -= booking.seats_booked
            show.save()
            booking.show = show
            booking.save()
            return redirect("home")
    else:
        form = BookingForm()

    return render(request, "book_ticket.html", {"show": show,"form":form})

