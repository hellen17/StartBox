from django import views
from django.urls import path
from . import views

#from frontend import views as views

from .views import HomeView, PackageView, GetTemplateView, DataPrivacyView, OnlineBUsinessView, Contact, register

app_name = 'StartBx.apps.frontend'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('packages/', PackageView.as_view(), name='packages'),
    path('templates/', GetTemplateView.as_view(), name='templates'),
    path('data-privacy/', DataPrivacyView.as_view(), name='dataprivacy'),
    path('online-business-package/', OnlineBUsinessView.as_view(), name='onlinebusinesspackage'),
    path('contact/', Contact.as_view(), name='contact'),
   

    # Auth urls
    path('register/', views.register, name='signup')
    #path('register/', Register.as_view(), name='register')
    

]
