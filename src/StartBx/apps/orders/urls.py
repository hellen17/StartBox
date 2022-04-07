from django.urls.conf import path
from . import views

app_name = 'orders'
urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
]