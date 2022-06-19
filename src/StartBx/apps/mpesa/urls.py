from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path


router = DefaultRouter()
router.register('transactions', views.MpesaTransactionViewset, basename='transactions')
app_name = 'mpesa'

urlpatterns = [
    path('mpesa/',views.mpesa_transactions , name='mpesa'),
]

urlpatterns +=router.urls