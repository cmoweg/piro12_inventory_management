from django.db import models


# Create your models here.

class Seller(models.Model):
    seller_name = models.CharField(max_length=20)
    seller_phone = models.CharField(max_length=13)
    seller_address = models.CharField(max_length=30)

    def __str__(self):
        return self.seller_name


class Product(models.Model):
    product_name = models.CharField(max_length=20)
    # product_img = models.ImageField()
    product_desc = models.TextField()
    product_price = models.IntegerField(blank=False, null=False)
    product_stock = models.IntegerField(blank=False, null=False)

    product_sell = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
