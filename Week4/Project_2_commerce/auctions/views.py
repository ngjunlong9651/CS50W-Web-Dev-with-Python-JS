from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing


def index(request):
    return render(request, "auctions/index.html")



def createListing(request):
    if request.method == "GET":
        allCategory = Category.objects.all()
        return render(request, "auctions/create.html", {
            "categories": allCategory
        })
        ## LHS is things we call in HTML, RHS is things we call in python
    else:
        ## Getting data from the form when user uses POST
        currentUser = request.user
        title = request.POST["title"]
        description = request.POST["description"]
        imageURL = request.POST["imageURL"]
        category = request.POST['category']
        price = request.POST['price']
        ## Need to check for current user as well 

        ## Get all content for new listing category 
        categoryData = Category.objects.get(categoryName = category)

        ## New Listing Object
        newListing = Listing(
            title = title, 
            description = description,
            imageURL = imageURL,
            price = float(price),
            category = categoryData,
            owner = currentUser
        )
        ## Insert objects into your database
        newListing.save()
        ## Return user to the index page
        return HttpResponseRedirect(reverse(index))
        

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
