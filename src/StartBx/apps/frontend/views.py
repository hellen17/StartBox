from re import template
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm, UserRegisterForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# auth views

# def register(response):
#     if response.method == 'POST':
#         form = UserRegisterForm(response.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(response, f'Your account has been created!')
#         return redirect('/')    
#     else:        
#         form = UserRegisterForm()
#     return render(response, 'registration/register.html', {'form': form})

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!')
            return redirect('/')


    else:   
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form':form})
 
 
# class Register(View):
#     def post(self, request):
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()  
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your account has been created! You are nowable to log in')
#             return redirect('login')
        
#         form = UserRegisterForm()
#         return render(request, 'register.html', {'form':form})



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