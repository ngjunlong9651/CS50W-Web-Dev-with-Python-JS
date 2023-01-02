from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="entry"),
    path("new_page", views.new_page, name="new_page"), ## Creating a page to contain new_pages function which will be added later on
    path("random_page", views.random_page, name="random_page") ## Creating a page to contain new_pages function which will be added later on
]
