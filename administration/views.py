from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .forms import ProductForm
import logging

logger = logging.getLogger(__name__)

# On importe les modèles.
from main.models import Product, Picture, Category

# Create your views here.
def adminhome(request):
    
    context = {}

    return render(request, "adminhome.html", context)


def add_product(request):

    context = {}

    form = ProductForm(request.POST, request.FILES)
    context['form'] = form

    if form.is_valid():
        
        datas = form.cleaned_data

        name, price, city = datas['name'], datas['price'], datas['city']
        quantity, availability = datas['quantity'], datas['availability']
        description, pictures = datas['description'], request.FILES.getlist('pictures')
        category = datas['category']

        product = Product(name=name, price=price, city=city, quantity=quantity, \
                        description=description, availability=availability)
        
        product.slug = slugify(product.name)
        product.save()

        # On ajoute les catégories.
        import karim.functions as f
        categories = f.parse_select_multiple(category)

        for cat in categories:
            _cat = get_object_or_404(Category, name=cat)
            product.category.add(_cat)
        
        # On ajoute les images.
        for key, img in enumerate(pictures):
            if key == 0:
                product.image = "products/" + str(img)

            product.save()
            pic = Picture(product=product, picture=img)
            pic.save()
            f.handle_upload_file("products", str(img), img)
            


    return render(request, "add_product.html", context)