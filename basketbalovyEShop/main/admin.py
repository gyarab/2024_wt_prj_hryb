from django.contrib import admin
from .models import Produkt, Brand

class ProduktAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "brand"]

class BrandAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "year"]

# Register your models here.
admin.site.register(Produkt, ProduktAdmin)
admin.site.register(Brand, BrandAdmin)