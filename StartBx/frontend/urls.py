from django.urls import path
from .views import HomeView, PackageView

app_name = 'frontend'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('packages/', PackageView.as_view(), name='packages')

]