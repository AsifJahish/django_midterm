from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from users.models import CustomUser
from .models import Product, Cart, CartItem

class ProductTestCase(TestCase):
    def setUp(self):
        self.seller = CustomUser.objects.create_user(username='seller', user_type='seller', password='pass123')
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=100.0,
            stock_quantity=10,
            category="Test Category",
            created_by=self.seller
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.created_by, self.seller)

class CartTestCase(TestCase):
    def setUp(self):
        self.buyer = CustomUser.objects.create_user(username='buyer', user_type='buyer', password='pass123')
        self.cart = Cart.objects.create(buyer=self.buyer)

    def test_cart_creation(self):
        self.assertEqual(self.cart.buyer.username, 'buyer')
