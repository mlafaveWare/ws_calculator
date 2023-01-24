from django.http import HttpResponse, HttpResponseBadRequest,HttpResponseServerError
from django.shortcuts import render

# Create your views here.from django.urls import path

def post(request):
    #post inputs
    #logic to determine min sq feet needed each year for 5 years
    if request != HttpResponseBadRequest:
        return HttpResponse("you need X sq ft 5 years from today to maintain your workspace")
    else:
        return HttpResponseServerError("server side error")
