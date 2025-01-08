from django.contrib import admin

from .models import Category, Tag, Product

admin.site.register(Category)  # Register the Category model
admin.site.register(Tag)  # Register the Tag model
admin.site.register(Product)  # Register the Product model
