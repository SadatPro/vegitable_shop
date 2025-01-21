from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Vegetable
from .forms import VegetableForm



def add_vegetable(request):
    if request.method == 'POST':
        form = VegetableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dashboard')
    else:
        form = VegetableForm()
    return render(request, 'vegetable_shop/add_vegetable.html', {'form': form})



def dashboard(request):
    vegetables = Vegetable.objects.all()
    return render(request, 'vegetable_shop/dashboard.html', {'vegetables': vegetables})

def edit_product(request, product_id):
    vegetable = get_object_or_404(Vegetable, id=product_id)
    if request.method == 'POST':
        form = VegetableForm(request.POST, request.FILES, instance=vegetable)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dashboard')
    else:
        form = VegetableForm(instance=vegetable)
    return render(request, 'vegetable_shop/edit_product.html', {'form': form})

def delete_product(request, product_id):
    vegetable = get_object_or_404(Vegetable, id=product_id)
    if request.method == 'POST':
        vegetable.delete()
        return redirect('dashboard:dashboard')
    return render(request, 'vegetable_shop/delete_product.html', {'vegetable': vegetable})
