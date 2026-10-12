"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
import json
from billing.engine import calculate_receipt

@csrf_exempt
def billing_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        receipt = calculate_receipt(data.get("pizzas", []))
        return JsonResponse({"receipt": receipt})
    return JsonResponse({"error":"POST required"}, status=405)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/billing/', billing_view, name='billing'),
]
