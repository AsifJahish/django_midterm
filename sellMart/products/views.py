from rest_framework import generics, permissions
from .models import Product, Cart, CartItem
from .serializers import ProductSerializer, CartSerializer, CartItemSerializer
from .permissions import IsSeller, IsBuyer
from rest_framework.exceptions import PermissionDenied

# Product Views
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsSeller]

    def perform_create(self, serializer):
        # Ensure the user is a seller before creating the product
        if self.request.user.user_type != 'seller':
            raise PermissionDenied("You are not authorized to add products.")
        serializer.save(created_by=self.request.user)

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

# Cart Views
class CartDetailView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated, IsBuyer]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(buyer=self.request.user)
        return cart

class CartItemAddView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsBuyer]

    def perform_create(self, serializer):
        if self.request.user.user_type != 'buyer':
            raise PermissionDenied("Only buyers can add items to the cart.")
        cart, created = Cart.objects.get_or_create(buyer=self.request.user)
        serializer.save(cart=cart)

class CartItemRemoveView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsBuyer]

    def get_queryset(self):
        if self.request.user.user_type != 'buyer':
            raise PermissionDenied("Only buyers can remove items from the cart.")
        cart = Cart.objects.get(buyer=self.request.user)
        return cart.items



# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

# Product Views
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
def product_create(request):
    if request.user.user_type != 'seller':
        return redirect('product-list')  # Redirect to the product list if not a seller
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect('product-list')  # Redirect to the product list after successful creation
    else:
        form = ProductForm()

    return render(request, 'product_add.html', {'form': form})
