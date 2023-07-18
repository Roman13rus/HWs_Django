from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = request.GET.get('page', 1)
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        reader_list = [page for page in reader]

        paginator = Paginator(reader_list, 10)
        page = paginator.get_page(page_number)
        bus_stations = page.object_list
        context = {
            'bus_stations': bus_stations,
            'page': page,
        }
    return render(request, 'stations/index.html', context)
