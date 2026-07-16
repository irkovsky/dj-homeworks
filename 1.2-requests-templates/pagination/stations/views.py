from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        all_stations = list(reader)
    
    page_obj = Paginator(all_stations, 10)
    
    page_number = request.GET.get('page')
    
    page = page_obj.get_page(page_number)

    context = {
         'bus_stations': page.object_list,
         'page': page,
    }
    
    return render(request, 'stations/index.html', context)
