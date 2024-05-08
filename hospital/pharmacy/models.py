from django.db import models
import random
import string
from django.utils import timezone

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

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)  # Ensure names are unique
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(default=timezone.now)
