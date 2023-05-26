from django.shortcuts import render
from random import randint
from django.http import HttpResponse

from . import models

def home_page(request):
    city_pk = request.GET.get("city")
    print(city_pk)
    cities = models.City.objects.filter(pk__lt=50)
    html = "<ul>"
    for city in cities:
        html += f"<li>{city.pk} City {city.name}</li>"
    html += "</ul>"   
    return HttpResponse (html)
#R

def view_city(request, pk):
    city = models.City.objects.get(pk=int(pk))
    html = f"City PK:{city.pk} City name {city.name}"
    return HttpResponse(html)
#D
def delete_city(request, pk):
    models.City.objects.get(pk=int(pk)).delete()
    return HttpResponse(f"Object {pk} has been deleted!")

    
