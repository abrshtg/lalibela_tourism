# lalibela_tourism/tourism/forms.py

from django import forms
from .models import Attraction

class AttractionForm(forms.ModelForm):
    class Meta:
        model = Attraction
        fields = ['name', 'description', 'location']
