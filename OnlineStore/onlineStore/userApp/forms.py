from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Buyer, Seller

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    user_type = forms.ChoiceField(choices=[('buyer', 'Buyer'), ('seller', 'Seller')])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']

class BuyerProfileForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['shipping_address', 'billing_address']

class SellerProfileForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['company_name', 'tax_id']