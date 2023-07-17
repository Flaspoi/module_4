from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")

def top_sellers(request):
    return render(request, "top-sellers.html")

def advertisement_post(request):
    return render(request, "advertisement-post")

def register(request):
    return render(request, "register")

def login(request):
    return render(request, "login")

def profile(request):
    return render(request, "profile")

def exit(request):
    return render(request, "exit")