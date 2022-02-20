from re import template
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.views import View

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class PackageView(TemplateView):
    template_name = 'packages.html'    

class GetTemplateView(TemplateView):
    template_name = 'documents.html'   

class DataPrivacyView(TemplateView):
    template_name = 'documents/dataprivacy.html'   

class OnlineBUsinessView(TemplateView):
    template_name = 'packages/online business.html'  

# class ProfessionalHelpView(TemplateView):
#     template_name = 'contact.html'  

class Contact(View):
    def get(self, request):
        form = ContactForm()
        return render(
            request, 'contact.html', {'form': form}
        )

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            return render(
            request,
            'contact.html',
            {'form': form},
        )
        return render(
            request,
            'contact.html',
            {'form': form})