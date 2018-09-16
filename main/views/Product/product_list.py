from django.shortcuts import render
from main.models import Product, Category


def product_list(request):

    context = {}

    datas = {}

    categories = Category.objects.filter(visible=True)

    for category in categories:
        
        datas[category.name] = Product.objects.filter(category=category, visible=True)

    context['datas'] = datas

    return render(request, 'product_list.html', context)
