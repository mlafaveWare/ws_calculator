import enum
import io
import sys

import form as form
from django.views.generic.edit import FormView,Form
from django.http import HttpResponse, HttpResponseBadRequest,HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render
from django.template.response import (
    TemplateResponse
)

# Create your views here.from django.urls import path


class FlowRatioView(FormView):

    red = 1.3
    orange = 1.45
    green = 1.6

    def get(self, request, *args, **kwargs):
        return TemplateResponse(
            request, self.template_name,{
                'title': 'FlowRatioView Page',
                'page_id': 'form-class-id',
                'page_class': 'form-class-page',
                'h1_tag': 'This is the FlowRatioView Page using Contact Form',
                'form': self.form_class


        }
        return TemplateResponse(
            request, self.template_name, {
                'form':self.form_class(initial)
            }
        )
    def post(self, request, *args, **kwargs):
        flow_factor = str(sys.argv[3])
        square_footage = str(sys.argv[2])




        if form.is_valid():
            return HttpResponseRedirect(
                self.success_url
            )
        else:
            return TemplateResponse(
           request,
           self.template_name,
           {
               'title': 'FormRatioView Page - Please correct errorws below',
               'page_id': 'form-class-id'
           }
       )

    #post inputs
    #logic to determine min sq feet needed each year for 5 years


