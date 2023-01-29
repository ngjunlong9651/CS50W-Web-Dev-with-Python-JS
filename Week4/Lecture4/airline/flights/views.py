from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from .models import Flights, Passengers
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'flights/index.html',{
        "flights": Flights.objects.all()
    })


def flight(request, flight_id):
    flight = Flights.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passengers.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers,
        "non_passengers": non_passengers
    })



def book(request, flight_id):

    # For a post request, add a new flight
    if request.method == "POST":

        # Accessing the flight
        flight = Flights.objects.get(pk=flight_id)

        # Finding the passenger id from the submitted form data
        passenger_id = int(request.POST["passenger"])

        # Finding the passenger based on the id
        passenger = Passengers.objects.get(pk=passenger_id)

        # Add passenger to the flight
        passenger.flights.add(flight)

        # Redirect user to flight page
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
>>>>>>> 4a05ac1eccc5b3880cb458b7ad7bebc8679b2532
