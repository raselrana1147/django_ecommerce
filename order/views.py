from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def order(request):
    return HttpResponse("this is order page")
