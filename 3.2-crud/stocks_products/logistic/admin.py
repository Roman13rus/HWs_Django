from logistic.models import Product, Stock, StockProduct
from django.contrib import admin

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass

@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    pass
