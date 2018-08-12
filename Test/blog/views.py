from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.

def do_normal(request):
    print("in the noraml")
    return HttpResponse("This is NormalMap")

def withparam(request,year,month):
    print("in the data")
    return HttpResponse("today is {0} year {1} month".format(year,month))

def findNumber(request,pagenumber):
    return HttpResponse("Page is number {0}".format(pagenumber))

def extraparam(request,name):
    return HttpResponse("My name is {0}".format(name))

def revParse(request):
    return HttpResponse("Request URl is {0}".format(reverse("askname")))