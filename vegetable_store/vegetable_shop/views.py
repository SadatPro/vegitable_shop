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
            return redirect('dashboard')
    else:
        form = VegetableForm()
    return render(request, 'vegetable_shop/add_vegetable.html', {'form': form})

def edit_vegetable(request, pk):
    vegetable = get_object_or_404(Vegetable, pk= pk)
    if request.method == "POST":
        form = VegetableForm(request.POST, request.FILES, instance=vegetable)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VegetableForm(instance=vegetable)
    return render(request, 'vegetable_shop/edit_vegetable.html', {'form': form})
