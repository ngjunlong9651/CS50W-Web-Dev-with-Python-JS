from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edit/", views.edit, name="edit"),
    path("save_edit/", views.save_edit, name="save_edit"),
    path("<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"), ## Must put a / at the back so that it is redirected to the appropriate page
    path("new_page/", views.new_page, name="new_page"), ## Creating a page to contain new_pages function which will be added later on
    path("random_page", views.random_page, name="random_page") ## Creating a page to contain new_pages function which will be added later on
]

