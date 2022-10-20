from django.contrib.sitemaps import Sitemap
from StartBx.apps.frontend.models import Product
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return [
            'frontend:home', 
            'frontend:packages',
            'frontend:templates',
            'frontend:contact',
            ]

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Product.objects.all()

