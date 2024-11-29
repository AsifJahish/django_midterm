from django.contrib import admin

from .models import Product, Cart, CartItem

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)

# from django.contrib import admin
# from .models import Product, Cart, CartItem

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'price', 'stock_quantity', 'created_by')
#     search_fields = ('name', 'category')
#     list_filter = ('category', 'created_by')
#     readonly_fields = ('created_at', 'updated_at')
