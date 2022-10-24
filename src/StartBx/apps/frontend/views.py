from re import template
import uuid
import environ
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm, UserRegisterForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.views.generic import DetailView, ListView,UpdateView
from airtable import Airtable
from decouple import config

base_key = config('AIRTABLE_BASE_KEY')
api_key = config('AIRTABLE_API_KEY')

# Create your views here.

# auth views

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Your account has been created!')
            return redirect('/cart')

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

class LandingPage(TemplateView):
    template_name = 'index.html' 

# class PackageView(TemplateView): 
#     template_name = 'packages.html'  

class GetPackageView(ListView):
    model = Product
    template_name = 'packages.html'
    slug_field = 'slug'
    extra_context={'packages': Product.objects.all().filter(category='Package')}


class GuidelinesView(TemplateView):
    template_name = 'comingsoon.html'     

class ViewProfileView(TemplateView):
    template_name = 'view_profile.html'

class OrderSuccessView(TemplateView):
    template_name = 'order-completed.html'

# class GetTemplateView(ListView):
#     model = Product
#     template_name = 'documents.html'
#     slug_field = 'slug'
#     extra_context={'templates': Product.objects.all().filter(category='Template')}


class TemplateMixin(object):
    def get_templates(self):
        return Product.objects.all().filter(category='Template')

    def get_context_data(self, **kwargs):
        context = super(TemplateMixin, self).get_context_data(**kwargs)
        context['templates'] = self.get_templates()
        return context    

class GetTemplateView(TemplateMixin, ListView):
    model = Product
    template_name = 'documents.html'
    slug_field = 'slug'

 
 
# class DataPrivacyView(TemplateView):
#     template_name = 'documents/dataprivacy.html'   

def DataPrivacyView(request):
    template = Product.objects.all().order_by('id')
    # print("This is a ", template)
    return render(request, 'documents/dataprivacy.html', context= {'template': template})


class OnlineBusinessView(ListView):
    model = Product
    template_name = 'packages/online business.html' 
    slug_field = 'slug'  
    extra_context={'templates': Product.objects.all().filter(category='Template')}



class Contact(View):
    table = config("AIRTABLE_CONTACT_TABLE")
    airtable = Airtable(base_key,table, api_key)

    def get(self, request):
        form = ContactForm()
        return render(
            request, 'contact.html', {'form': form}
        )

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.company_name = form.cleaned_data['company_name']
            #form.nature_of_business = form.cleaned_data['nature_of_business']
            form.contact_name = form.cleaned_data['contact_name']
            form.phone_number = form.cleaned_data['phone_number']
            form.email = form.cleaned_data['email']
            #form.save()

            '''add airtable code here'''
            try:
                self.airtable.insert({
                    'Company name': form.cleaned_data['company_name'],
                    #'Business nature': form.cleaned_data['nature_of_business'],
                    'Name': form.cleaned_data['contact_name'],
                    'Phone Number': form.cleaned_data['phone_number'],
                    'Email': form.cleaned_data['email'],
                    'Message': form.cleaned_data['message'],
                })
            except Exception as e:
                print('Error',e) 
    
            messages.success(request, "Form submitted successfully") 
            return redirect('frontend:contact') 
        return render(
            request,
            'contact.html',
            {'form': form})


# Cart
# This Code is not in use #
def view_cart(request):
    cart_data = {}
    prices = []
    total = 0
    order = Order.objects.filter(customer_id=uuid.UUID('e49b7fd2-584e-4e14-b710-a36a1441bf3d'), purchased=False).values().first() 

    if order is None:
        print('None')
    else:
        order_id = order['order_id']

        order_details = OrderDetail.objects.filter(order_id=str(order_id)).values()

        # print(order_details)

        for order_detail in order_details:
            current_order_detail = order_detail['order_detail_id']
            # print(order_detail)
            current_product_id = order_detail['product_id']
            # print(current_product_id)

            product_detail = Product.objects.filter(product_id=current_product_id).values().first()

            # print(product_detail)
            product_price = product_detail['product_price']
            quantity = order_detail['quantity']
            subtotal = product_price * quantity

            prices.append(subtotal)

            single_item_order = {
                "product_id": current_product_id,
                "product_name": product_detail['product_name'],
                "product_image": product_detail['product_pictures'],
                "product_price": product_price,
                "quantity": order_detail['quantity'],
                "subtotal": subtotal
            }

            cart_data.update({str(current_order_detail): single_item_order})

        for price in prices:
            total+=price
        # Display in Cart for Item: Order_detail_id, Product_id, Product Name, Product Image, Price, Quantity 

    return render(request, 'shopping-cart.html', context= {'cart_details': cart_data, 'total': total})
    # print(products)
    # return render(request, 'index.html', {'product_list': products, 'media_url':settings.MEDIA_URL})


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'product_detail.html'
#     slug_field = 'slug'
#     # extra_context={'template': Product.objects.filter(slug=slug_field)}


def package_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    package = Product.objects.all().filter(category='Package')
    context = {
        'object': product,
        'dataset': package,
    }
    
    return render(request, 'package_detail.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    template = Product.objects.all().filter(category='Template')
    context = {
        'object': product,
        'dataset': template,
    }

    return render(request, 'product_detail.html', context)    


def search(request):        
    if request.method == 'GET':      
        template_name =  request.GET.get('search','')    
        try:
            status = Product.objects.filter(product_name__icontains=template_name) # filter returns a list so you might consider skip except part
            print('Status',status)
            return render(request,"documents.html",{"templates":status})
        except:
            status = None
            print('Status',status)

            return render(request,"documents.html",{'templates':status})
    else:
        return render(request,"documents.html",{})

#edit template
class UpdateTemplateView(UpdateView):
    model = Product
    fields = ['content']
    template_name = 'edit-template.html'

   