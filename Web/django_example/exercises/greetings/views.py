from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import admin
from django.urls import path

# Create your views here.


def hello_world(request):
    return HttpResponse("Hello World!")

def hello_name(request, name):
    return HttpResponse(f"Hello {name}")