from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement


def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, "index.html")

def top_sellers(request):
    return render(request, "top-sellers.html")

def advertisement_post(request):
    return render(request, "advertisement-post.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def profile(request):
    return render(request, "profile.html")

def exit(request):
    return render(request, "exit.html")