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




# @login_required
# def add_to_cart(request, product_id):
#     if request.user.user_type != 'buyer':
#         return JsonResponse({'error': 'Only buyers can add items to the cart.'}, status=403)

#     product = get_object_or_404(Product, id=product_id)
#     cart, created = Cart.objects.get_or_create(buyer=request.user)
#     cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

#     if not item_created:  # If the item already exists in the cart, increase the quantity
#         cart_item.quantity += 1
#         cart_item.save()

#     return JsonResponse({'message': f'{product.name} added to cart.', 'cart_item_count': cart_item.quantity})


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem

@login_required
def add_to_cart(request, product_id):
    # Get the product to be added to the cart
    product = get_object_or_404(Product, id=product_id)

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(buyer=request.user)

    # Add the product to the cart (if it already exists, increase the quantity)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    # If the item already exists in the cart, increase its quantity
    if not item_created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1  # Ensure quantity is set to 1 if it's a new item

    # Save the cart item with the correct quantity
    cart_item.save()

    # Redirect the user to the cart items page (where they can view the cart)
    return redirect('cart-items')  # Make sure this URL name matches your cart items page URL


@login_required
def cart_items(request):
    if request.user.user_type != 'buyer':
        return redirect('product-list')  # Redirect non-buyers to the product list

    cart, created = Cart.objects.get_or_create(buyer=request.user)
    items = cart.items.select_related('product')  # Optimize query with related data

    return render(request, 'cart_items.html', {'items': items})
