from django.db import models
from django.contrib.auth.models import User
from app.categories.models import Category


class Transaction(models.Model):
    class Type(models.TextChoices):
        INCOME = 'income', 'Ingreso'
        EXPENSE = 'expense', 'Gasto'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    type = models.CharField(max_length=7, choices=Type.choices)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='transactions')
    description = models.TextField(blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.get_type_display()} - ${self.amount} ({self.date})"
