from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Map to the product_list view
]
