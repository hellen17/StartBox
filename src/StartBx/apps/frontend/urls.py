from django import views
from django.urls import path
#from . import views
from .views import *
from django.contrib.auth import views as auth_views
from django.urls.conf import include

# from .views import HomeView, PackageView, GetTemplateView, DataPrivacyView, OnlineBUsinessView, Contact, register,view_cart, ProductDetailView

app_name = 'StartBx.apps.frontend'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('index/', LandingPage.as_view(), name='landing'),
    path('packages/', GetPackageView.as_view(), name='packages'),
    path('templates/', GetTemplateView.as_view(), name='templates'),
    path('guidelines/', GuidelinesView.as_view(), name='guidelines'),

    path('data-privacy/', DataPrivacyView, name='dataprivacy'),
    path('online-business-package/', OnlineBusinessView.as_view(), name='onlinebusinesspackage'),
    path('contact/', Contact.as_view(), name='contact'),
    # path('template/<slug:slug>/', ProductDetailView.as_view(), name="product-detail"),
    path('template/<slug:slug>/', product_detail, name="product-detail"),
    path('template/edit/<slug:slug>/', UpdateTemplateView.as_view(), name="edit-template"),

    path('packages/<slug:slug>/', package_detail, name="package-detail"),
    path('profile/', ViewProfileView.as_view(), name='profile'),
    path('order-success/', OrderSuccessView.as_view(), name='order-success'),
    path('search/', search, name='search'),
    #path('transactions/', include("StartBx.apps.mpesa.urls", namespace="transactions")),

    #path('cart/',view_cart, name="cart"),
    # Auth urls
    path('register/', register, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view())
    #path('register/', Register.as_view(), name='register')

    

]
