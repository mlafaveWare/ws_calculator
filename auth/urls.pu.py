from django.urls import re_path
from django.views.generic import (
    TemplateView
)

from . views import Auth_Class_View

urlpatterns = [
    re_path(
        r'^auth/auth-class'
    )
]