from django.contrib import admin
from .models import Order, Customer
# Register your models here.
@admin.register(Customer)
class Customer(admin.ModelAdmin):
    pass

@admin.register(Order)
class Order(admin.ModelAdmin):
    pass
