import form as form
from django import forms
from django.forms import Form, ModelForm

class Auth_Class(ModelForm):
    full_name = form.CharField(
        label = 'Full Name',
        help_text = 'Enter Your Username and Password',
        min_length = 2,
        max_length = 300,
        required = True,
        error_messages = {
            'required': 'Please correct your login information',
            'min_length': 'Please lengtehn your name',
            'max_length': 'Character max exceeded. Please reduce input'
        },

        widget = forms.TextInput(
            attrs = {
                'id' : 'full-name',
                'class': 'form-input-class'
            }
        )
    )