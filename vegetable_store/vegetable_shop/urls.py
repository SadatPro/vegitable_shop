from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_vegetable, name='add_vegetable'),
    path('edit/<int:pk>/', views.edit_vegetable, name='edit_vegetable'),
]
