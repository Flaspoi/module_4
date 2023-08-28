from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import Advertisement
from .forms import AdvertisementForm


def index(request):
    advertisements = Advertisement.objects.all()
    context = {"advertisements": advertisements}
    return render(request, "app_advertisements/index.html", context=context)


def top_sellers(request):
    return render(request, "app_advertisements/top-sellers.html")


@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = form.save(commit=False)
            # advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    form = AdvertisementForm()
    context = {"form": form}
    return render(request, "app_advertisements/advertisement-post.html", context)
