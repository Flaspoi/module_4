from django.db import models


class Advertisement(models.Model):
    title = models.CharField(
        verbose_name="Заголовок",
        max_length=100,
        )
    description= models.TextField(
        verbose_name="Описание",
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=2
    )
    auction = models.BooleanField(
        verbose_name="Торг",
        default=False,
        help_text="Отметьте, если торг уместен!"
    )
    created_at = models.DateTimeField(
        verbose_name="Дата добавления",
        auto_now_add = True,
    ),
    updated_at = models.DateTimeField(
        verbose_name="Дата редактирования",
        auto_now=True,
    )
