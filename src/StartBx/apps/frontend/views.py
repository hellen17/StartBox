from re import template
import uuid
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm, UserRegisterForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.views.generic import DetailView, ListView


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

class GetTemplateView(ListView):
    model = Product
    template_name = 'documents.html'  
    slug_field = 'slug'
    #extra_context={'templates': Product.objects.all()}

 


# class DataPrivacyView(TemplateView):
#     template_name = 'documents/dataprivacy.html'   

def DataPrivacyView(request):
    template = Product.objects.all().order_by('id')
    # print("This is a ", template)
    return render(request, 'documents/dataprivacy.html', context= {'template': template})


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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    slug_field = 'slug'
    # extra_context={'template': Product.objects.filter(slug=slug_field)}


def product_detail(request, pk):
    product = get_object_or_404(Product, pk)
    context = {
        'template': product,
    }
    return render(request, 'product_detail.html', context)