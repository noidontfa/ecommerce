from django import forms
from django.forms import fields, widgets
from .models import Cart

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__' 
        widgets = {
            'product': forms.HiddenInput(),
            'user_other': forms.HiddenInput()
        }