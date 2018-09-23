from django.views.generic import TemplateView
from django.http import HttpResponse
from main.models import Category, Product


class HomePage(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        categories = Category.objects.all()[:6]

        products = Product.objects.filter(visible=True, quantity__gt=0)[:20]

        covers = [{'url': c.image.url, 'text': c.name, 'description': c.description} for c in categories]

        context['categories'] = categories
        context['products'] = products
        context['covers'] = covers
        context['home'] = True

        return context
