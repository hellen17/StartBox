from . import views
from django.urls import path

app_name = 'payment'
urlpatterns = [
    path("process-mpesa", views.payment_process_mpesa, name="process-mpesa"),
    path("process-card", views.payment_process_card, name="process-card"),
    
    path("pay-mpesa",views.process_mpesa, name="pay-mpesa"),
]