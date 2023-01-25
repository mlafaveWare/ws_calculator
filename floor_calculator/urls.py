from django.urls import path

from . import views

urlpatterns = [
    path("floor_calulcator/", views.index), # if a request reaches floor_calc, exe function pointed to by views.index
    path("floor_calulcator/", views.post),
    path("floor_calulcator/", views.update()),
    path("floor_calulcator/", views.get()),
    path("floor_calulcator/", views.delete())
    ]