from django.urls import path
from . import views

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),
    path('nueva/', views.transaction_create, name='transaction_create'),
    path('<int:pk>/editar/', views.transaction_edit, name='transaction_edit'),
    path('<int:pk>/eliminar/', views.transaction_delete, name='transaction_delete'),
]
