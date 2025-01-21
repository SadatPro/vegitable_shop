from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from vegetable_shop.models import Vegetable

def vegetable_list(request):
    vegetables = Vegetable.objects.all()
    return render(request, 'shop/vegetable_list.html', {'vegetables': vegetables})
