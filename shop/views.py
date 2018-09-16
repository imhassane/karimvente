from django.shortcuts import render, get_object_or_404 as _g
from shop.models import Order, Bucket
from main.models import Product

from django.http import JsonResponse
from django.utils.text import slugify


# Create your views here.
def add_to_bucket(request, product_pk):
    
    # On ajoute la clé validated dans la session.
    request.session['validated'] = False

    
    product = _g(Product, pk=product_pk)

    order = Order(product=product)
    order.save()

    bucket = request.session['bucket']
    bucket.append(order.pk)

    request.session['bucket'] = bucket

    return JsonResponse({
        'message': "Votre commande a été ajoutée",
        "order_count": len(request.session['bucket'])
    })

def del_from_bucket(request, order_pk):
    
    order = _g(Order, pk=order_pk)
    
    bucket = request.session['bucket']
    bucket.remove(order_pk)

    request.session['bucket'] = bucket
    
    order.delete()

    request.session['validated'] = False

    return JsonResponse({
        'message': "La commande a été supprimée"
    })

def validate_order(request):
    
    context = {}

    try:

        # Si la session existe.
        if request.session['bucket'] and len(request.session['bucket'])!= 0 and not request.session['validated']:
            
            # On regroupe toutes les commandes dans un panier.
            bucket = Bucket()
            bucket.sent = True
            bucket.save()

            total_price = 0

            for order in request.session['bucket']:
                _order = _g(Order, pk=order)
                bucket.order.add(_order)

                total_price += _order.product.price
            
            bucket.value = total_price
            bucket.save()

            # On ajoute la clé validated dans la session.
            request.session['validated'] = True

            # On vide le panier.
            del request.session['bucket']

            context['message'] = "Votre commande a été enregistrée, nous reviendrons vers vous pour entamer la démarche nécessaire"
    
    except:
        
        # On va afficher un message d' erreur.
        context['message'] = "Une erreur s'est produite lors de la validation de votre commande"

    return JsonResponse(context)

def bucket(request):
    
    context = {}

    try:

        bucket = [_g(Order, pk=pk) for pk in request.session['bucket']]
        context['bucket'] = bucket
        context['total_price'] = sum([x.product.price for x in bucket]) if len(bucket) > 0 else 0
    
    except:

        request.session['bucket'] = []

    return render(request, "bucket.html", context)


# Validation de la commande par l'administrateur
import accounts.views.decorators as decorators
import django.contrib.auth.decorators as auth

@auth.user_passes_test(decorators.user_is_admin)
def show_orders(request):

    context = {}

    buckets = Bucket.objects.filter(validated=False, sent=True)
    context['buckets'] = buckets
    context['total_buckets'] = buckets.count()

    return render(request, "show_buckets.html", context)
