from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("save_customer/", views.customer, name="customer")
]