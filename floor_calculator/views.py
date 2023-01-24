from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseForbidden,HttpResponseServerError
from django.http import Http404
# Create your views here.

def index(request):
    return HttpResponse("Working")
