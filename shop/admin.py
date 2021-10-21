from django.contrib import admin
from shop.models import Product, Category, Order, Mapping


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Mapping)