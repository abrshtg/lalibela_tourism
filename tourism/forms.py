from django import forms
from .models import Attraction, Booking, TourPackage, Tourist


class AttractionForm(forms.ModelForm):
    class Meta:
        model = Attraction
        fields = ["name", "description", "location", "image"]


class TouristForm(forms.ModelForm):
    class Meta:
        model = Tourist
        fields = ["name", "email", "phone_number"]


class TourPackageForm(forms.ModelForm):
    class Meta:
        model = TourPackage
        fields = ["name", "description", "price"]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["tourist", "tour_package", "date_booked", "num_people"]
        widgets = {"date_booked": forms.DateTimeInput(attrs={"type": "datetime-local"})}
