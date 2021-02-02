
from django.shortcuts import render
from .models import Announcment

def index(request):
    announcment = Announcment.pobjects.all()
    return render(request, "index.html", {"announcments": announcment})

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def blog(request):
    return render(request, "blog.html")

def agents(request):
    return render(request, "agents.html")

def properties(request):
    return render(request, "properties.html")