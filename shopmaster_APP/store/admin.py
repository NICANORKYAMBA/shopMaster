from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stars']
    search_fields = ['name', 'category']
    list_filter = ['category', 'price']
    list_editable = ['price', 'stars']
    list_per_page = 5