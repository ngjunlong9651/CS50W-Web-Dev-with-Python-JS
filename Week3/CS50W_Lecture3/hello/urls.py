from django.urls import path
from . import views ## from current directory import views.py


urlpatterns = [
    path("", views.index, name ="index"), ## when user enters the url "", return the page known as views.index. the page shall be named index
    path("ashley", views.ashley, name="ashley"),
    path("jl", views.jl, name ="jl"),
    path("<str:name>", views.greet, name="greet")
]