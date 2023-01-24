from django.urls import path

from . import views

urlpatterns = [
    path("floor_calculator", views.index) # if a request reaches floor_calc, exe function pointed to by views.index
]