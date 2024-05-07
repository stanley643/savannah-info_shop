from django.db import models
import random
import string
class Customer(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5, unique=True, primary_key=True)
    phone_number = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        if not self.code:
            # Generate a random unique code of four digits and a random letter
            digits = ''.join(random.choices(string.digits, k=4))
            letter = random.choice(string.ascii_letters)
            self.code = f"{digits}{letter}"
        super().save(*args, **kwargs)

class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Ensure names are unique
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Convert the name to lowercase before saving to ensure case-insensitivity
        self.name = self.name.lower()
        super().save(*args, **kwargs)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(choices=[(i, i) for i in range(1, 21)])
    time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if the order is being created
            self.amount = self.item.amount * self.quantity  # Calculate the amount
        super().save(*args, **kwargs)


