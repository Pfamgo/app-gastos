from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='categories')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
