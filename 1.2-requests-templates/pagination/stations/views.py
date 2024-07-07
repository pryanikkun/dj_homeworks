from csv import DictReader
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    station_list = []
    with open(
            settings.BUS_STATION_CSV, 'r', newline='', encoding='utf-8'
    ) as f:
        reader = DictReader(f)
        for row in reader:
            station_list.append(
                {'Name': row['Name'],
                 'Street': row['Street'],
                 'District': row['District']}
            )
    paginator = Paginator(station_list, 10)
    page = paginator.get_page(int(request.GET.get('page', 1)))
    context = {
        'page': page,
    }
    return render(request, 'stations/index.html', context)
