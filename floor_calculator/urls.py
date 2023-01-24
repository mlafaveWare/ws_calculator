from django.urls import path

from . import views

urlpatterns = [
    path("floor_calculator", views.index), # if a request reaches floor_calc, exe function pointed to by views.index
    path("floor_calculator", views.post),
    path("floor_calculator", views.update()),
    path("floor_calculator", views.get()),
    path("floor_calculator", views.delete())
    ]