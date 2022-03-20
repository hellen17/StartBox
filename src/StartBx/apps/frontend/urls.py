from django import views
from django.urls import path
from . import views

#from StartBx.apps.frontend import views as views

#from frontend import views as views

from .views import HomeView, PackageView, GetTemplateView, DataPrivacyView, OnlineBUsinessView, Contact, register,view_cart, ProductDetailView

app_name = 'StartBx.apps.frontend'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('packages/', PackageView.as_view(), name='packages'),
    path('templates/', GetTemplateView.as_view(), name='templates'),
    path('data-privacy/', DataPrivacyView, name='dataprivacy'),
    path('online-business-package/', OnlineBUsinessView.as_view(), name='onlinebusinesspackage'),
    path('contact/', Contact.as_view(), name='contact'),
    path('product/<int:pk>/detail/', ProductDetailView.as_view(), name="product-detail"),

    #path('cart/',view_cart, name="cart"),
   

    # Auth urls
    path('register/', views.register, name='signup')
    #path('register/', Register.as_view(), name='register')
    

]
