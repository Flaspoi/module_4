from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.db.models import Count

from .models import Advertisement
from .forms import AdvertisementForm


User = get_user_model()


def index(request):
    title = request.GET.get("query")
    if title:
        advertisements = Advertisement.objects.filter(title__icontains=title)
    else:
        advertisements = Advertisement.objects.all()

    context = {"advertisements": advertisements, 'title': title}
    return render(request, "app_advertisements/index.html", context=context)


def top_sellers(request):
    users = User.objects.annotate(
        adv_count=Count("advertisement")
    ).order_by("-adv_count")
    context = {
        "users": users
    }
    return render(request, "app_advertisements/top-sellers.html", context=context)


@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    form = AdvertisementForm()
    context = {"form": form}
    return render(request, "app_advertisements/advertisement-post.html", context)


def advertisement_view(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    context = {
        "advertisement": advertisement
    }
    return render(request, "app_advertisements/advertisement.html", context=context)