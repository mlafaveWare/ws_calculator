from django.urls import path

from . import views


urlpatterns = [
   path("<str:flow_calculation>", views.flow_calculator())
   path("<str:flow_calculator")
]