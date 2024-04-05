from django.contrib import admin

from products.models import ProductCategory,Product
from users.models import User

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(User)