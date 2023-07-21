from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_obj = Phone.objects.all()
    if request.GET.get('sort') == 'name':
        phones_list = sorted(phones_obj, key=lambda phone: phone.name)
        context = {'phones': phones_list}
        return render(request, template, context)
    elif request.GET.get('sort') == 'min_price':
        phones_list = sorted(phones_obj, key=lambda phone: phone.price)
        context = {'phones': phones_list}
        return render(request, template, context)
    elif request.GET.get('sort') == 'max_price':
        phones_list = sorted(phones_obj, key=lambda phone: phone.price, reverse=True)
        context = {'phones': phones_list}
        return render(request, template, context)
    context = {'phones': phones_obj}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
