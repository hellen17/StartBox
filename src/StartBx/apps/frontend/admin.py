from django.contrib import admin
from . models import Product,Packages

 

class PackageModelInline(admin.TabularInline):
    model = Packages

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = [PackageModelInline]
    

admin.register(Packages)
