from django.urls import path
from .import views

urlpatterns =[
    path('',views.home, name='home'),
    path('add-movie/',views.add_movie,name='add_movie'),
    path('add-show/',views.add_show,name='add_show'),
    path('movie/<int:movie_id>/',views.movie_detail,name="movie_detail.html"),path("book/<int:show_id>/", views.book_ticket, name="book_ticket"),
]