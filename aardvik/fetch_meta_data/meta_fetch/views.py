from django.shortcuts import render
from django.http import HttpResponse
#from http.client import HTTPResponse
# Create your views here.

def home(request):
    return HttpResponse("Hey, this is meta_fetch")