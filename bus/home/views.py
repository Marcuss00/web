from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "index.html")
def customer(request):
   if request.method =='POST' :
        try :
           first_name=request.POST["first_name"]
           last_name=request.POST["last_name"]
           name = first_name +last_name 
           age = request.POST["age"]
           password=request.POST("password")
           sql = "INSERT INTO customer(first_name, last_name, age, password) VALUES(%s,%s,%s,%s);"
           
           return HttpResponse(f"name is {name}")
        except KeyError:
            return HttpResponse("something is missing")
   else:
       return HttpResponse("only accepts post method")