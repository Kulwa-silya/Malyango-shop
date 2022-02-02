from django.contrib import admin
from .models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','price','active','category','created','updated']
    list_filter = ['created','updated','active']
    list_editable = ['price','active']
    prepopulated_fields = {'slug':('product_name',)}
