from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from billing.models import Order, Pizza, Topping, Price

@csrf_exempt
def billing_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        order = Order.objects.create()
        for p in data.get("pizzas", []):
            pizza = Pizza.objects.create(order=order, size=p.get("size", "Medium"))
        return JsonResponse({"order_id": order.id, "receipt": "v2 receipt"})
    if request.method == "GET":
        order_id = request.GET.get("order_id")
        order = Order.objects.get(id=order_id) if order_id else None
        if order:
            pizzas = order.pizzas.all()
            items = [{"size": p.size, "toppings": [i.topping.name for i in p.items.all()], "price": 0.0} for p in pizzas]
            receipt = "\n".join([f"{i['size']} - {', '.join(i['toppings']) or 'No toppings'}" for i in items])
            return JsonResponse({"order_id": order.id, "receipt": receipt, "items": items})
        return JsonResponse({"error": "order_id required"}, status=400)
    return JsonResponse({"error":"method not allowed"}, status=405)
