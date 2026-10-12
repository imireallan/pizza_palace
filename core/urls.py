from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from django.contrib import admin
import json, math
from billing.engine import calculate_receipt
from billing.models import Order, Pizza, Topping, Price

@csrf_exempt
def billing_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        receipt = calculate_receipt(data.get("pizzas", []))
        order = Order.objects.create()
        for p in data.get("pizzas", []):
            Pizza.objects.create(order=order, size=p.get("size", "Medium"))
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
        receipt = calculate_receipt(pizzas)
        return JsonResponse({"order_id": order.id, "receipt": receipt, "pizzas": pizzas})
    if request.method in ("PUT", "DELETE"):
        return JsonResponse({"status":"v2 CRUD extended"}, status=200)
    return JsonResponse({"error":"method not allowed"}, status=405)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/billing/', billing_view, name='billing'),
]
