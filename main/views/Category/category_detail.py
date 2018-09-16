from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404 as _g
from main.models import Category, Product


def category_detail(request, slug):

    context = {}

    category = _g(Category, slug=slug)
    context['category'] = category
    context['products'] = Product.objects.filter(category=category)

    page = request.GET.get('page', 1)

    paginator = Paginator(context['products'], 2)

    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    
    context['numbers'] = numbers

    return render(request, 'category_detail.html', context)
