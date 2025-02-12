from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def january(request):
    return HttpResponse("Eat no carbs for the entire month!")


def february(request):
    return HttpResponse("Walk for at least 20 minutes everyday!")


def march(request):
    return HttpResponse("Learn Django for at least 20 minutes everyday!")