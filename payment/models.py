from django.db import models


class Item(models.Model):
    """Объект покупки."""

    name = models.CharField("Название", max_length=255, null=False, blank=False)
    description = models.TextField("Описание", null=True, blank=True)
    price = models.DecimalField(
        "Цена", max_digits=12, decimal_places=2, null=False, blank=False
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"{self.name}"
