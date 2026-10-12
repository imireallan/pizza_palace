from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order, Pizza
from .serializers import OrderSerializer, OrderCreateSerializer, PizzaSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related('pizzas__items__topping').all()

    def create(self, request, *args, **kwargs):
        serializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        output_serializer = OrderSerializer(order)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderCreateSerializer
        return OrderSerializer

class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.select_related('order').prefetch_related('items__topping').all()
    serializer_class = PizzaSerializer
