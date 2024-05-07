from django.contrib import admin
from .models import Order, Customer, Item
# Register your models here.
@admin.register(Customer)
class Customer(admin.ModelAdmin):
    pass

@admin.register(Order)
class Order(admin.ModelAdmin):
    pass


@admin.register(Item)
class Item(admin.ModelAdmin):
    pass