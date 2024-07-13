from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    sort_options = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    if sort:
        phones = Phone.objects.all().order_by(sort_options.get(sort))
    else:
        phones = Phone.objects.all()
    template = 'catalog.html'
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
