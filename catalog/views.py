from django.shortcuts import render
from django.db.models import Q
from .models import Product, Category, Tag

def product_list(request):
    # Start with all products
    products = Product.objects.all().prefetch_related('tags')

    # Apply filtering by description
    query = request.GET.get('q', '')
    if query:
        products = products.filter(description__icontains=query)

    # Apply filtering by category
    categories = Category.objects.all()
    category_filter = request.GET.get('category', '')
    if category_filter:
        products = products.filter(category__name=category_filter)

    # Apply filtering by tags
    tags = Tag.objects.all()
    tags_filter = request.GET.getlist('tags', [])
    if tags_filter:
        for tag in tags_filter:
            products = products.filter(tags__name=tag)

    return render(request, 'catalog/product_list.html', {
        'products': products,
        'categories': categories,
        'tags': tags,
        'selected_tags': tags_filter,  # Pass the selected tags to the template
    })
