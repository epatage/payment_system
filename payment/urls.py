from django.urls import path

from .views import buy_item, cancel_payment, index, item_info, success_payment


app_name = "payment"

urlpatterns = [
    path("success/", success_payment, name="success_payment"),
    path("cancel/", cancel_payment, name="cancel_payment"),
    path("buy/<int:item_id>/", buy_item, name="buy_item"),
    path("item/<int:item_id>/", item_info, name="item_info"),
    path("", index, name="index"),
]
