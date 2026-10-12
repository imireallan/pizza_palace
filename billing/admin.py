from django.contrib import admin
from .models import Order, Pizza, Topping, Price, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'receipt_text')
    readonly_fields = ('created_at',)

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'size')

@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'basic')

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'size', 'base')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'pizza', 'topping')
