
from django.db import models
from django.utils import timezone
from StartBx.apps.frontend.models import Product

from dataclasses import dataclass

@dataclass(frozen=True)
class PaymentOptions:
    MPESA:str = 'MPESA'
    CARD: str = 'CARD'

# Create your models here.

class Order(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    payment_method = models.CharField(max_length=50, default=PaymentOptions.MPESA)
    mpesa_code = models.CharField(max_length=50, blank=True)
    braintree_id = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100, default="")
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created",)

    def __str__(self) -> str:
        return f"Order {self.id}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE, null=True,blank=True
    )
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.id}"

    def get_cost(self):
        return self.price * self.quantity
