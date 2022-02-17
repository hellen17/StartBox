from django.urls import path
from .views import HomeView, PackageView, GetTemplateView, DataPrivacyView, OnlineBUsinessView
#from . import views
app_name = 'frontend'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('packages/', PackageView.as_view(), name='packages'),
    path('templates/', GetTemplateView.as_view(), name='templates'),
    path('dataprivacy/', DataPrivacyView.as_view(), name='dataprivacy'),
    path('onlinebusinesspackage/', OnlineBUsinessView.as_view(), name='onlinebusinesspackage'),
    

]
