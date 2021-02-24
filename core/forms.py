from django import forms
from django.forms import fields
from .models import Cart

class CartForm(forms.ModelForm):
    product = forms.HiddenInput() 
    user_other = forms.HiddenInput()
    class Meta:
        model = Cart
        fields = '__all__' 