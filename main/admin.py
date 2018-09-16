from django.contrib import admin
from main.models import Category, Product, Picture, Witness


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Picture)
admin.site.register(Witness)
