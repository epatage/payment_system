import os

import stripe
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET
from dotenv import load_dotenv

from .models import Item


load_dotenv()

STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")
stripe.api_key = STRIPE_API_KEY


def index(request):
    """Главная страница со всеми товарами."""

    items = Item.objects.all()

    return render(request, "index.html", {"items": items})


def success_payment(request):
    """Оповещает об успешной оплате товара."""

    return render(request, "success.html")


def cancel_payment(request):
    """Оповещает об отказе от оплаты товара."""

    return render(request, "cancel.html")


@require_GET
def buy_item(request, item_id):
    """Вызывает форму оплаты товара."""

    item = get_object_or_404(Item, pk=item_id)

    session = stripe.checkout.Session.create(
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": f"{item.name}",
                    "description": f"{item.description}",
                },
                "unit_amount": f"{item.price}".replace(".", ""),
            },
            "adjustable_quantity": {"enabled": True},
            "quantity": 1,
        }],
        mode="payment",
        success_url="http://127.0.0.1:8000/success",
        cancel_url="http://127.0.0.1:8000/cancel",
    )

    return redirect(session.url)


@require_GET
def item_info(request, item_id):
    """Отдает страницу товара с информацией и кнопкой для покупки."""

    item = get_object_or_404(Item, pk=item_id)

    context = {"item": item}

    return render(request, "item_info.html", context)
