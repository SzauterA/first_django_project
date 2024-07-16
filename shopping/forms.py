from django import forms
from .models import Customer
from .models import Products

class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required=False, help_text="Enter last name")
    email = forms.EmailField(max_length=200, required=False, widget=forms.TextInput(attrs={'placeholder': 'Email'}))

"""
class CustomerRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    age = forms.IntegerField()
    phone = forms.CharField(max_length=200, required=False)
"""

class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        #fields = ['first_name', 'last_name', 'email', 'age', 'phone']
        fields = '__all__'
        #exclude = ['phone']
    
class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, required=False)
    #price = forms.DecimalField(max_digits=5, decimal_places=0, required=False)

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['price', 'is_discounted', 'storage_quantity']