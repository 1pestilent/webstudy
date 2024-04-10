from django.contrib import admin

from products.models import ProductCategory,Product, Basket
from users.models import User

admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','quantity','category']
    fields = ('name', 'description',('price','quantity'),'category', 'image')
    search_fields = ('name',)
    ordering = ('name', )

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product','quantity','created_timestamp',)
    readonly_fields = ('created_timestamp',)
    extra = 0