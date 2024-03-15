from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=100)
    number = forms.CharField(max_length=15)
    email = forms.EmailField()
