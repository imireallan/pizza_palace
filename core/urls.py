from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from billing.views_drf import OrderViewSet, PizzaViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'pizzas', PizzaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
