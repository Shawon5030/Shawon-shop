from django.db import models
from django.utils.text import slugify

# Create your models here.
catagory_choice = [
    ('baby fashion' , 'baby fashion'),
    ('health & beauty', 'health & beauty'),
    ('electronics', 'electronics'),
    ('mens fashion', 'mens fashion'),
    ('women fashion', 'women fashion'),
]

class product_model(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    decounted_price = models.IntegerField()
    brand = models.CharField(max_length=20)
    
    
    category = models.CharField(max_length=20 , choices=catagory_choice)


class banner(models.Model):
    name = models.CharField(max_length=30 , null=True, blank=True)
    image = models.ImageField(upload_to='banners/' )

    def __str__(self):
        return self.name 