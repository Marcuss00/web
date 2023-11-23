from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("book_bus/", views.book_bus, name="book_bus")
]