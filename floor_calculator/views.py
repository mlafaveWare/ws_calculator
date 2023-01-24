from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseForbidden,HttpResponseServerError
from django.http import Http404
# Create your views here.

def index(request):
    return HttpResponse("Working")

def post(request):
    if request != HttpResponseBadRequest:
        #.write(request)
        return HttpResponse("Request Posted")
    else:
        return("server side error")

def delete(request, id,):
        #if request != HttpResponseBadRequest and id != HttpResponseBadRequest:
      #object.delete/flush(id)

    #else
    #return HttpResponseBadRequest
    return HttpResponse("Record deleted")
def update(request, id):
    if request != HttpResponseBadRequest and id != HttpResponseBadRequest:
    #HttpResponse.write(request, id)
        return HttpResponse("Request Updated")
    else:
        return ("error 500")

def get(request, id):
    if request != HttpResponseBadRequest and id != HttpResponseBadRequest:
        #return object.id
        return HttpResponse("Here is your get request")
    else:
        return("server side error")