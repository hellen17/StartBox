from django.urls import path
#from frontend import views as views

from .views import HomeView, PackageView, GetTemplateView, DataPrivacyView, OnlineBUsinessView, Contact

app_name = 'frontend'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('packages/', PackageView.as_view(), name='packages'),
    path('templates/', GetTemplateView.as_view(), name='templates'),
    path('data-privacy/', DataPrivacyView.as_view(), name='dataprivacy'),
    path('online-business-package/', OnlineBUsinessView.as_view(), name='onlinebusinesspackage'),
    path('contact/', Contact.as_view(), name='contact'),
    

]
