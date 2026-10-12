from rest_framework import serializers
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
        order = Order.objects.create(**validated_data)
        for p in pizzas_data:
            pizza = Pizza.objects.create(order=order, size=p.get('size', 'Medium'))
            for t in p.get('toppings', []):
                topping_obj, _ = Topping.objects.get_or_create(name=t, defaults={"basic": t in {"Cheese","Pepperoni","Ham","Pineapple"}})
                OrderItem.objects.create(pizza=pizza, topping=topping_obj)
        return order
