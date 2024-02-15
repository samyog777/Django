from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#for using a whole file inside of the python
def index(request):
    return render(request, "hello/index.html")

# For using html code inside the python
def samyog(request):
    return HttpResponse("Hello Samyog")

# Using Whole file inside the python using render
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
    