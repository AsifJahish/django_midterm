from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Product

def home(request):
    return render(request, 'products/homep.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user  # Associate product with the logged-in user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})



def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('product_list')  # Redirect back to the product list
    
    # Not expecting a GET request here
    return redirect('product_detail', pk=pk)
