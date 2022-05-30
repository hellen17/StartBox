from django.shortcuts import redirect, render

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
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        payment_method = request.POST.get("payment-method")
        # breakpoint()
        if form.is_valid():
            order = form.save()
            order.payment_method = payment_method
            order.save()
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
        form = OrderCreateForm()
    return render(request, "shop-checkout.html", {"cart": cart, "form": form})



