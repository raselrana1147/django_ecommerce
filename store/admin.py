from django.contrib import admin
from store.models import Category,Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	

admin.site.register(Category)
admin.site.register(Product)
