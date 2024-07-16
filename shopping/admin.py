from django.contrib import admin

# Register your models here.

from .models import Customer, Products, Purchase, Address, PurchaseItem 
from django.db import models

from .filters import PriceRangeFilter, CustomerFilterByAge
from .filters2 import GenericIntegerRangeFilter, PriceRangeFilter, QuantityRangeFilter

class PurchaseInLine(admin.StackedInline):
    model = Purchase
    extra = 1

class AddressInLine(admin.StackedInline):
    model = Address
    extra = 1

class PurchaseItemInLine(admin.StackedInline):
    model = PurchaseItem
    extra = 1

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'age')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = (CustomerFilterByAge,)
    ordering = ('first_name', 'last_name', 'age')
    readonly_fields = ('email',)
    inlines = [PurchaseInLine, AddressInLine]
    #exclude = ('phone',)
    fieldsets = (
        ('Name', {
            'fields': ('first_name', 'last_name')
        }),
        ('Contact Info', {
            'fields': ('email', 'phone')
        }),
        ('Other', {
            'fields': ('age',)
        })
    )

def set_discounted(modeladmin, request, queryset):
    print(modeladmin)
    print(request)
    print(queryset)
    count = queryset.update(is_discounted=True)
    modeladmin.message_user(request, f'Updatedproducts: {count}')

set_discounted.short_description = 'Set selected products as discounted'

class ProductsAdmin(admin.ModelAdmin):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    list_display = ('name', 'price', 'is_discounted')
    list_filter = ()
    actions = [set_discounted]
    actions_on_top = True
    actions_on_bottom = True


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('purchase_date', 'customer')
    inlines = [PurchaseItemInLine]
    raw_id_fields = ('customer',)



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Address)
admin.site.register(PurchaseItem)
