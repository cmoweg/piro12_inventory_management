from django.db import models


# Create your models here.

class Seller(models.Model):
    seller_name = models.CharField(max_length=20)
    seller_phone = models.CharField(max_length=13)
    seller_address = models.GenericIPAddressField()

class Product(models.Model):
    product_name = models.CharField(max_length=20)
    # product_img = models.ImageField()
    product_desc = models.TextField
    product_price = models.IntegerField(blank=False, null=False)
    product_stock = models.IntegerField(blank=False, null=False)

    product_sell = models.ForeignKey(Seller, on_delete=models.CASCADE)
