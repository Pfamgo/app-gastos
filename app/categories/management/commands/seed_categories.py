from django.core.management.base import BaseCommand
from app.categories.models import Category


DEFAULT_CATEGORIES = [
    'Comida',
    'Transporte',
    'Ocio',
    'Salud',
    'Servicios',
    'Educación',
    'Ropa',
    'Hogar',
    'Otros',
]


class Command(BaseCommand):
    help = 'Crea las categorías predefinidas'

    def handle(self, *args, **options):
        for name in DEFAULT_CATEGORIES:
            Category.objects.get_or_create(name=name, user=None)
            self.stdout.write(self.style.SUCCESS(f'Categoría "{name}" creada.'))
