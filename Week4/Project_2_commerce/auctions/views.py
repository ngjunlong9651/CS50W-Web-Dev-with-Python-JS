from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing, Comment, Bid


def index(request):
    activelistings = Listing.objects.filter(isActive = True)
    allCategory = Category.objects.all()
    return render(request, "auctions/index.html",{
        "listings": activelistings,
        "categories": allCategory,
    })
    ##LHS is referred to by HTML, RHS is referred to by python

def addBid(request, id):
    newBid = int(request.POST['newBid'])
    listingData = Listing.objects.get(pk=id)
    isOwner = request.user.username == listingData.owner.username
    isListingInWatchlist = request.user in listingData.watchlist.all() ## Check if user is in the watchlist
    allComments = Comment.objects.filter(listing=listingData)
    if newBid > listingData.price.bid:
        updateBid = Bid(user=request.user, bid = newBid)
        updateBid.save()
        listingData.price = updateBid
        listingData.save()
        return render(request,"auctions/listing.html",{
            "listing": listingData,
            "message": "Bid was successfully updated!",
            "update": True,
            "isOwner": isOwner ,
            "isListingInWatchList" : isListingInWatchlist,
            "allComments" : allComments
        })

    else:
        return render(request,"auctions/listing.html",{
            "listing": listingData,
            "isOwner": isOwner,
            "message": "Bid was NOT successfully updated!",
            "update": False,
            "isListingInWatchList" : isListingInWatchlist,
            "allComments" : allComments
        })

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


        ## Need to create a bid object for new listing
        bid = Bid(bid = int(price), user = currentUser)
        bid.save()
        ## Get all content for new listing category 
        categoryData = Category.objects.get(categoryName = category)

        ## New Listing Object
        newListing = Listing(
            title = title, 
            description = description,
            imageURL = imageURL,
            price = bid,
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

def listing(request, id):
    listingData = Listing.objects.get(pk=id)
    isListingInWatchlist = request.user in listingData.watchlist.all() ## Check if user is in the watchlist
    allComments = Comment.objects.filter(listing=listingData)
    isOwner = request.user.username == listingData.owner.username
    return render(request, "auctions/listing.html",{
        "listing":listingData,
        "isListingInWatchlist" : isListingInWatchlist,
        "allComments":allComments,
        "isOwner": isOwner
    })


def closeAuction(request, id):
    listingData = Listing.objects.get(pk=id)
    listingData.isActive = False
    listingData.save()
    isOwner = request.user.username == listingData.owner.username
    return render(request, "auctions/listing.html",{
    "listing":listingData,
    "update": True,
    "message": "Congratulations, your auction has been closed!",
    "isOwner": isOwner  
    })


def displayCategory(request):
    if request.method == "POST":
        chosenCategory = request.POST["category"]
        category = Category.objects.get(categoryName = chosenCategory)
        activelistings = Listing.objects.filter(isActive = True, category = category)
        allCategory = Category.objects.all()
        return render(request, "auctions/index.html",{
            "listings": activelistings,
            "categories": allCategory,
    })
    ##LHS is referred to by HTML, RHS is referred to by python

def watchlist(request):
    currentuser = request.user
    listings = currentuser.listingWatchlist.all()
    return render(request, "auctions/watchlist.html",{
        "listings" : listings
    })

    #currentUser = request.user
    #listings = currentUser.listingWatchlist.all()
    #return render(request, "auctions/watchlist.html")

def removeWatchList(request,id):
    listingData=Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing", args =(id, )))

def addWatchList(request,id):
    listingData= Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing", args = (id, )))

def addComment(request, id):
    currentUser = request.user
    listingData = Listing.objects.get(pk=id)
    message = request.POST['newComment']

    newComment = Comment(
        author = currentUser,
        listing = listingData,
        message = message
    )

    newComment.save()

    return HttpResponseRedirect(reverse("listing", args = (id, )))
 