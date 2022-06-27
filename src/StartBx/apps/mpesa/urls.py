from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path


router = DefaultRouter()
router.register('transactions', views.MpesaTransactionViewset, basename='transactions')
app_name = 'mpesa'

urlpatterns = [
 
]

urlpatterns +=router.urls