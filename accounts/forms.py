from django.forms import ModelForm
from .models import Order, Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__' # All the fields will be created.

''' to specify the fields for the form.
use list to specify particular field,
 for example fields = ['products', 'date_created'] '''

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
