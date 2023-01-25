from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import FormView

from . import forms
from .forms import User
from django.template.response import (
    TemplateResponse
)

class Auth_Class_View(FormView):
    template_name = 'ws_calculator/auth/form-class.html'
    form_class = User
    success_url = '/auth/auth-form-success'

    def get(self, request, *args, **kwargs):
        pass
