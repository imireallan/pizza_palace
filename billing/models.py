from django.db import models

SIZE_CHOICES = [("Small", "Small"), ("Medium", "Medium"), ("Large", "Large")]

class Topping(models.Model):
    name = models.CharField(max_length=50)
    basic = models.BooleanField(default=True)

class Price(models.Model):
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    base = models.DecimalField(max_digits=8, decimal_places=2)

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class Pizza(models.Model):
    order = models.ForeignKey(Order, related_name="pizzas", on_delete=models.CASCADE)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)

class OrderItem(models.Model):
    pizza = models.ForeignKey(Pizza, related_name="items", on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
