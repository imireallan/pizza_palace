from django.db import models

SIZE_CHOICES = [("Small","Small"),("Medium","Medium"),("Large","Large")]

class Topping(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    receipt_text = models.TextField(blank=True, default="")

class Pizza(models.Model):
    order = models.ForeignKey(Order, related_name="pizzas", on_delete=models.CASCADE)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)

class OrderItem(models.Model):
    pizza = models.ForeignKey(Pizza, related_name="items", on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
