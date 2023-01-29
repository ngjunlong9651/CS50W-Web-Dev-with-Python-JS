from django.urls import path
<<<<<<< HEAD
from . import views
urlpatterns = [
    
=======

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book")

>>>>>>> 4a05ac1eccc5b3880cb458b7ad7bebc8679b2532
]