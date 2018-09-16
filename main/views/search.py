from django.shortcuts import render
from main.models import Product, Category


def search(request):

    question = request.GET['q']

    context = {}

    categories = Category.objects.filter(name__icontains=question)
    products = Product.objects.filter(name__icontains=question)

    context['categories'] = categories
    context['products'] = products


    return render(request, 'forms/search_results.html', context)
