from django.test import TestCase
from core.models import Item,UserProfile,OrderItem,Address
from django.db import models
from django.conf import settings
from unittest.mock import patch

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
    
class UserProfileTestCase(TestCase):

    def setUp(self):
        self.obj = UserProfile(stripe_customer_id="123456789",one_click_purchasing=True) 

    def testStripeCustomerId(self):
        self.assertEqual(self.obj.stripe_customer_id,"123456789","Stripe customer id should be same")

    def testOneClickPurchase(self):
        self.assertEqual(self.obj.one_click_purchasing,True,"Stripe customer id should be same")


class OrderItemTestCase(TestCase):

    def setUp(self):
        Item.objects.create(title="New Product",price=100.0,category="SW",label="P",slug="test-product",discount_price=400)       
        self.obj = OrderItem(ordered=True,item=Item.objects.get(),quantity=5) 

    def testPrice(self):
        self.assertEqual(self.obj.item.price,100.00)

    def testDiscountPrice(self):
        self.assertEqual(self.obj.item.discount_price,400)

    def testTotalPrice(self):
        self.assertEqual(self.obj.get_total_item_price(),500)

    def testTotalDiscountPrice(self):
        self.assertEqual(self.obj.get_total_discount_item_price(),2000.00)

    def testAmountSaved(self):
        self.assertEqual(self.obj.get_amount_saved(),-1500.00)
    
    def testGetFinalPrice(self):
        self.assertEqual(self.obj.get_final_price(),2000.00)


class AddressTestCase(TestCase):

    def setUp(self):
        self.obj = Address(street_address="800 N LBJ Drive",apartment_address="215",country="US",zip="78666",address_type="S") 

    def testStreetAddress(self):
        self.assertEqual(self.obj.street_address,"800 N LBJ Drive")

    def testApartmentAddress(self):
        self.assertEqual(self.obj.apartment_address,"215")

    def testCountry(self):
        self.assertEqual(self.obj.country,"US")
    
    def testZip(self):
        self.assertEqual(self.obj.zip,"78666")
    
    def testType(self):
        self.assertEqual(self.obj.address_type,"S")