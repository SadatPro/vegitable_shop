from django.urls import path
from . import views

urlpatterns = [
    path('', views.vegetable_list, name='vegetable_list'),
]
