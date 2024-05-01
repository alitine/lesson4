from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
"""
def index(request):
    return HttpResponse("Hello!")
"""

"""
def brian(request):
    return HttpResponse("Hello Brian!")

def david(request):
    return HttpResponse("Hello David!")
"""

"""
# Introduction to the views with placeholders in order to comment brian and david function
def greet(request, name):
    return HttpResponse(f"hello, {name.capitalize()}!")
"""


# PASS from HttpResponse to render
    # - create un folder "templates" in app1 folder / create another folder "app1"
    #   in templates folder refere to the "app1/index.html"
def index(request):
    return render(request,"app1/index.html")


def greet(request, name):
    return render(request, "app1/greet.html", {
        "name": name.capitalize()
    })