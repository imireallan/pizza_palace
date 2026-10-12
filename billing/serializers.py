from rest_framework import serializers
from .models import Order, Pizza, Topping, Price

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
