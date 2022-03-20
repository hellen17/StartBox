from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=40,null=False)
    product_description = models.CharField(max_length=500,null=False)
    price = models.FloatField()
    url = models.URLField()
    # brand = models.CharField(max_length=255,choices=BRAND_TYPES,default=None)
    # colour = models.CharField(max_length=255,choices=COLOR,default=None,null=True)
    # zipped = models.BooleanField(default=None)

    # image = models.ImageField(upload_to='product_images',null=True)

    def __str__(self):
            return self.product_name