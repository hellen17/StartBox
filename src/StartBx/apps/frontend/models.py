from django.db import models
from django.urls import reverse

from django.utils.text import slugify


# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=40,null=False)
    product_description = models.CharField(max_length=500,null=False)
    price = models.FloatField()
    url = models.URLField(null=True,blank=True)
    slug = models.SlugField(unique=True,null=True,blank=True)

    # brand = models.CharField(max_length=255,choices=BRAND_TYPES,default=None)
    # colour = models.CharField(max_length=255,choices=COLOR,default=None,null=True)
    # zipped = models.BooleanField(default=None)

    # image = models.ImageField(upload_to='product_images',null=True)

    def __str__(self):
            return self.product_name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.product_name)

            super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("StartBx.apps.frontend:product-detail", kwargs={"slug": self.slug})        

