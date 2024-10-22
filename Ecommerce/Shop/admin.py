from django.contrib import admin
from .models import *

@admin.register(product_model)
class ProductAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        # Get all field names
        fields = [field.name for field in self.model._meta.get_fields()]
        # Exclude 'description' field
        fields.remove('description')
        return fields
admin.site.register(banner)


@admin.register(Cart_model)

class CartAdmin(admin.ModelAdmin):
    list_display = ['user' , 'products','quantity']





        
