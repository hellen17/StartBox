from re import template
from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class PackageView(TemplateView):
    template_name = 'packages.html'    

class GetTemplateView(TemplateView):
    template_name = 'documents.html'   

class DataPrivacyView(TemplateView):
    template_name = 'documents/dataprivacy.html'      