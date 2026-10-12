from rest_framework import serializers
import math
from billing.engine import calculate_receipt, calculate_pizza_price
from .models import Order, Pizza, Topping, Price, OrderItem

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = '__all__'

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    pizzas = PizzaSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['receipt_text'] = instance.receipt_text or ret.get('receipt_text', '')
        ret['receipt'] = instance.receipt_text or ret.get('receipt', '')
        return ret

class OrderCreateSerializer(serializers.ModelSerializer):
    pizzas = serializers.JSONField(write_only=True)
    class Meta:
        model = Order
        fields = ('id', 'pizzas', 'receipt_text', 'created_at')
    def create(self, validated_data):
        pizzas_data = validated_data.pop('pizzas', [])
        priced = []
        for p in pizzas_data:
            price = calculate_pizza_price(p.get('size', 'Medium'), p.get('toppings', []))
            priced.append({"size": p.get('size', 'Medium'), "toppings": p.get('toppings', []), "price": price})
        receipt_text_value = calculate_receipt(priced) if priced else ""
        order = Order.objects.create(receipt_text=receipt_text_value, **validated_data)
        for p in pizzas_data:
            pizza = Pizza.objects.create(order=order, size=p.get('size', 'Medium'))
            for t in p.get('toppings', []):
                topping_obj, _ = Topping.objects.get_or_create(name=t, defaults={"basic": t in {"Cheese","Pepperoni","Ham","Pineapple"}})
                OrderItem.objects.create(pizza=pizza, topping=topping_obj)
        return order
