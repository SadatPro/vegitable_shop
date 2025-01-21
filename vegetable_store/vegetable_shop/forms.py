from django import forms
from .models import Vegetable

class VegetableForm(forms.ModelForm):
    class Meta:
        model = Vegetable
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width: 100%; padding: 10px; border-radius: 4px; border: 1px solid #ccc;'}),
            'description': forms.Textarea(attrs={'style': 'width: 100%; padding: 10px; border-radius: 4px; border: 1px solid #ccc;'}),
            'price': forms.NumberInput(attrs={'style': 'width: 100%; padding: 10px; border-radius: 4px; border: 1px solid #ccc;'}),
            'image': forms.ClearableFileInput(attrs={'style': 'width: 100%; padding: 10px; border-radius: 4px; border: 1px solid #ccc;'}),
        }
