from sre_constants import CATEGORY
from django.db import models
from django.urls import reverse

from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
#from django_ckeditor_5.fields import CKEditor5Field

# from markdown_deux import markdown
# from django.utils.safestring import mark_safe

CATEGORY = (
    ('Package', 'Package'),
    ('Template', 'Template'),
 
)


# Create your models here.

class Packages(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=40)# null is False by default
    product_description = models.CharField(max_length=500)
    content = RichTextUploadingField()
    #content = CKEditor5Field(null=True, config_name="extends")

    price = models.FloatField()
   # url = models.URLField(default="",blank=True)
    slug = models.SlugField(unique=True,default="",blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY)
    file = models.FileField(default="",blank=True)
    many_files=models.ManyToManyField(Packages,default="",blank=True)



    # brand = models.CharField(max_length=255,choices=BRAND_TYPES,default=None)
    # colour = models.CharField(max_length=255,choices=COLOR,default=None,null=True)
    # zipped = models.BooleanField(default=None)

    # image = models.ImageField(upload_to='product_images',null=True)

    def __str__(self):
            return self.product_name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.product_name)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("StartBx.apps.frontend:product-detail", kwargs={"slug": self.slug})      

    # def get_markdown(self):
    #     content = self.content
    #     markdown_text = markdown(content)
    #     return mark_safe(markdown_text)       

