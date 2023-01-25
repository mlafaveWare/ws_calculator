from django.urls import path, include

from . import views

urlpatterns = [
    path("flow_ratio/", views.index), # if a request reaches floor_calc, exe function pointed to by views.index
    path("flow_ratio/", views.post),
    path("flow_ratio/", views.update()),
    path("floor_ratio/", views.get()),
    path("floor_ratio/", views.delete())
]