from django.test import TestCase
from core.models import Item
from django.db import models

class ItemTestCase(TestCase):
    # Test Fixture
    def setUp(self):
        Item.objects.create(title="New Product",price=100.0,category="SW",label="P",slug="test-product")

    # Test Case
    def testMatchSlugUrl(self):
        obj = Item.objects.get()        
        self.assertEqual(obj.get_absolute_url(), "/product/test-product/", "Slug URL didn't matched")

    # Test Case
    def testMatchProductTitle(self):
        obj = Item.objects.get()       
        self.assertEqual(obj.title,"New Product","Title didn't match") 

    # Test Case
    def testMatchPrice(self):
        obj = Item.objects.get()       
        self.assertEqual(obj.price,100.0,"Price didn't match") 

    # Test Case 
    def testMatchAddToCartURL(self):
        obj = Item.objects.get()       
        self.assertEqual(obj.get_add_to_cart_url(),"/add-to-cart/test-product/","Add to Cart didn't match") 