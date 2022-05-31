from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from ian_cart.cart import Cart
from StartBx.apps.frontend.models import Product
from .forms import OrderCreateForm
from .models import Order, OrderItem, PaymentOptions
from django.urls import reverse
from .tasks import order_created
from django.contrib.auth.decorators import login_required

'''
If user has not logged in redirect them to login/register before checkout
'''

@login_required
def checkout(request):
    print("User is ", request.user)
    current_user = request.user
    cart = Cart(request)
   

    if request.method == "POST":

      
        form = OrderCreateForm(request.POST or None, instance=current_user)
        payment_method = request.POST.get("payment-method")
        print(form.errors)

        data = {            
                'first_name': current_user.first_name,
                'last_name' : current_user.last_name,
                'email': current_user.email,
                }
        form = OrderCreateForm(data)        

        # breakpoint()
        if form.is_valid():
            order = form.save()
            order.payment_method = payment_method
            order.save()
            print("Order is" , order)
            for item in cart:
                # breakpoint()
                product = Product.objects.get(id=item.get("product_id"))
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=item.get("price"),
                    # quantity=item.get("quantity"),
                )
            
            order_created.delay(order.id) # delay function adds the task to the queue
            # set the order in the session
    
            request.session["order_id"] = str(order.id)
            # redirect for payment
            if payment_method == PaymentOptions.MPESA:
                return redirect(reverse("payment:process-mpesa"))
            return redirect(reverse("payment:process-card"))
    else:
        # form.fields['first_name'].initial = current_user.first_name
        # form.fields['last_name'].initial = current_user.last_name
        # form.fields['email'].initial = current_user.email

        
        form = OrderCreateForm(
                #   initial={            
                #     'first_name': current_user.first_name,
                #     'last_name' : current_user.last_name,
                #     'email': current_user.email,
                #   }

        )
   

    return render(request, "shop-checkout.html", {"cart": cart, "form": form})



