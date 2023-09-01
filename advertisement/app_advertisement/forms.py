from django.forms import ModelForm
from .models import Advertisement


from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django import forms

from .models import Advertisement


# class AdvertisementForm(ModelForm):
#     class Meta:
#         model = Advertisement
#         fields = ["title", "description", "price", "auction", "image"]

#     def clean_title(self):
#         title = self.cleaned_data["title"]
#         if title.startswith("?"):
#             raise ValidationError("Заголовок начинается с ?")
#         return title
    
    


class AdvertisementForm(forms.Form):
    title = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"})
    )
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control form-control-lg"}))
    price = forms.DecimalField(widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}))
    auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control form-control-lg"}))