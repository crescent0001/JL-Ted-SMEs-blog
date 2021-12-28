from django import forms
from django.forms import ModelForm
from .models import Enquiry

class ContactForm(ModelForm):

    class Meta:
        model = Enquiry
        fields = ('name', 'email', 'mobile', 'Type_of_Enquiry', 'message')
        labels = {
            'name' : '',
            'email' : '',
            'mobile' : '',
            'Type_of_Enquiry' : '',
            'message' : '',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Enter Your Name'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control', 'placeholder': 'Enter Your Email'}),
            'mobile' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Enter Your Mobile Number'}),
            'Type_of_Enquiry' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Enter Your Enquiry'}),
            'message' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'What you wanna sasy to us???'}),

        }