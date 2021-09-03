from cars.models import Car
from django.shortcuts import render

def index(request):
    cars = Car.objects.all()
    return render(request, 'index.html', locals())


def generic(request):
    return render(request, 'generic.html', locals())


def elements(request):
    return render(request, 'elements.html', locals())