from django.views.generic import ListView
from main.models import Category, Product


class CategoryListView(ListView):


    model = Category
    template_name = ' category_list.html'
    context_object_name = 'categories'
