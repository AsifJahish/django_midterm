from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from users.models import CustomUser
from products.models import Product
from .models import Order, OrderItem

class OrderTestCase(TestCase):
    def setUp(self):
        self.buyer = CustomUser.objects.create_user(username='buyer', user_type='buyer', password='pass123')
        self.seller = CustomUser.objects.create_user(username='seller', user_type='seller', password='pass123')
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=100.0,
            stock_quantity=10,
            category="Test Category",
            created_by=self.seller
        )
        self.order = Order.objects.create(buyer=self.buyer)
        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
            item_price=self.product.price
        )
        self.order.update_total()

    def test_order_creation(self):
        self.assertEqual(self.order.total_amount, 200.0)
        self.assertEqual(self.order.status, 'pending')

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.total_price(), 200.0)
