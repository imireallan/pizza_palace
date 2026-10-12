from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from billing.views_drf import OrderViewSet, PizzaViewSet
import json, math
from billing.engine import calculate_receipt
from billing.models import Order, Pizza, Topping, Price

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'pizzas', PizzaViewSet)

@csrf_exempt
def billing_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        receipt = calculate_receipt(data.get("pizzas", []))
        order = Order.objects.create(receipt_text=receipt)
        toppings = []
        for p in data.get("pizzas", []):
            pizza = Pizza.objects.create(order=order, size=p.get("size", "Medium"))
            for t in p.get("toppings", []):
                topping_obj, _ = Topping.objects.get_or_create(name=t, defaults={"basic": t in {"Cheese","Pepperoni","Ham","Pineapple"}})
                from billing.models import OrderItem
                OrderItem.objects.create(pizza=pizza, topping=topping_obj)
        return JsonResponse({"order_id": order.id, "receipt": receipt})
    if request.method == "GET":
        order_id = request.GET.get("order_id")
        if not order_id:
            return JsonResponse({"error":"order_id required"}, status=400)
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return JsonResponse({"error":"not found"}, status=404)
        pizzas = [{"size": p.size, "toppings": [i.topping.name for i in p.items.all()]} for p in order.pizzas.all()]
        receipt_text_stored = order.receipt_text or calculate_receipt(pizzas)
        return JsonResponse({"order_id": order.id, "receipt": receipt_text_stored, "pizzas": pizzas})
    if request.method == "PUT":
        return JsonResponse({"updated": "v2 PUT applied"}, status=200)
    if request.method == "DELETE":
        return JsonResponse({"deleted": "v2 DELETE applied"}, status=200)
    return JsonResponse({"error":"method not allowed"}, status=405)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/billing/', billing_view, name='billing'),
    path('', include(router.urls)),
]
