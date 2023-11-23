from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
# Create your views here.

def home(request):
    return render(request, "index.html")

def book_bus(request):
    sql_query ="SELECT * FROM bus_schedule WHERE bus_number = %s"
    bus_number='UK07DU8357'

    with connection.cursor() as cursor:
        cursor.execute(sql_query, (bus_number,))
        bus_data =  cursor.fetchone()
        print(bus_data)
    return render(request, "book_bus.html" , {'bus_data':bus_data})