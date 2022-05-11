from django.shortcuts import render, redirect, get_object_or_404
from ian_cart.cart import Cart
from StartBx.apps.orders.models import Order
from django.conf import settings
import braintree
from django.urls import reverse
from .tasks import payment_completed
from django.contrib.auth.decorators import login_required


gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

# Create your views here.
def payment_process_card(request):
    cart = Cart(request)
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()
    if request.method == "POST":
        # retrieve nonce
        nonce = request.POST.get("payment_method_nonce", None)
        # create and submit transaction
        result = gateway.transaction.sale(
            {
                "amount": f"{total_cost:.2f}",
                "payment_method_nonce": nonce,
                "options": {"submit_for_settlement": True},
            }
        )
        if result.is_success:
            # mark the order as paid
            order.paid = True
            # store the unique transaction id
            order.braintree_id = result.transaction.id
            order.save()
            payment_completed.delay(order.id)
            cart.clear()
            return render(request, "order-completed.html", {"order": order})
        else:
            return redirect("/shop")
    else:
        # generate token
        client_token = gateway.client_token.generate()
        return render(
            request,
            "process-card.html",
            {"order": order, "client_token": client_token},
        )



def payment_process_mpesa(request):

    cart = Cart(request)
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, id=order_id)

    # if not request.user.is_authenticated():
    #     return redirect('/login')
    
    if request.method == "POST":
        # payment_process.delay(order_id)
        cart.clear()
        return redirect("/shop")
    return render(request, "process-mpesa.html", {"order": order})



def order_completed(request):
    return render(request, "order-completed.html")