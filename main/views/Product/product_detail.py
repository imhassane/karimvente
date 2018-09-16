from django.shortcuts import render, get_object_or_404 as _g
from django.http import JsonResponse
from main.models import Product, Picture, Category

def product_detail(request, slug):

    if request.POST:
        pass
    
    else:
        context = {}

        product = _g(Product, slug=slug)
        picture = Picture.objects.filter(product=product)

        context['product'] = product
        context['pictures'] = [ img.picture for img in picture]

        return render(request, 'product_detail.html', context)


def like_product(request, slug):
    
    product = _g(Product, slug=slug)

    product.like += 1

    product.save()

    return JsonResponse({'like': product.like})
