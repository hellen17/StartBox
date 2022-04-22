from django import views
from django.urls import path
#from . import views
from .views import *

# from .views import HomeView, PackageView, GetTemplateView, DataPrivacyView, OnlineBUsinessView, Contact, register,view_cart, ProductDetailView

app_name = 'StartBx.apps.frontend'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('packages/', PackageView.as_view(), name='packages'),
    path('templates/', GetTemplateView.as_view(), name='templates'),
    path('guidelines/', GuidelinesView.as_view(), name='guidelines'),

    path('data-privacy/', DataPrivacyView, name='dataprivacy'),
    path('online-business-package/', OnlineBUsinessView.as_view(), name='onlinebusinesspackage'),
    path('contact/', Contact.as_view(), name='contact'),
    # path('template/<slug:slug>/', ProductDetailView.as_view(), name="product-detail"),
    path('template/<slug:slug>/', product_detail, name="product-detail"),


    #path('cart/',view_cart, name="cart"),
    # Auth urls
    path('register/', register, name='signup')
    #path('register/', Register.as_view(), name='register')
    

]
