from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("payment.urls", namespace="payment")),
]

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Система оплаты товаров"
