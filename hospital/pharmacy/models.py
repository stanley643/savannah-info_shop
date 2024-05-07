from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True, primary_key=True)
    phone_number = models.CharField(max_length=15)

class Customer(User):
    user_ptr = models.OneToOneField(User, parent_link=True, on_delete=models.CASCADE)
class Item(models.Model):
    name = models.CharField(unique=True, max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(choices=[(i, i) for i in range(1, 21)])
    time = models.DateTimeField(auto_now_add=True)
