from struct import pack_into
from django.shortcuts import render, redirect, get_object_or_404
from ian_cart.cart import Cart
from StartBx.apps.orders.models import Order
from django.conf import settings
import braintree
from django.urls import reverse
from .tasks import payment_completed
from StartBx.apps.mpesa.utils import handle_stk_request
from django.contrib import messages
import time
#from StartBx.apps.mpesa.views import receive_callback



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
        #print("Result is",result)   

        if result.is_success:
            # mark the order as paid
            order.paid = True
            order.status = 'SUCCESSFUL'
            # store the unique transaction id
            order.braintree_id = result.transaction.id
            order.save()
            payment_completed.delay(order.id)
            cart.clear()
            return render(request, "order-completed.html", {"order": order})
        else:
            return redirect("/templates")
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
    print(f"Order : {order}")

 #
    if request.method == "POST":
        '''
        Add payment completed page with payment completed method
        '''
        #payment_process.delay(order_id)
        cart.clear()
        return redirect("/templates")
    return render(request, "process-mpesa.html", {"order": order})

''''
Create a view that takes user phone number that calls stk push and takes user to order success page if order is successful
'''

def process_mpesa(request):

    cart = Cart(request)
    order_id = request.session.get("order_id")
    #order = get_object_or_404(Order, id=order_id)
    order = Order.objects.get(id=order_id)

    print(f"Order : {order}")

 #
    if request.method == "POST":
        '''
        Add payment completed page with payment completed method
        '''
        phone_number = request.POST.get("phone_number")

        response = handle_stk_request(phone_number=phone_number,amount=str(order.get_total_cost()),reference=order.id)
        print("Response is:", response)

        '''
        TODO:
        Add code to check if transaction was successful  before redirecting 
        the user to order success page
        '''
        # cart.clear()
        # messages.success(request, "Payment was successful")
        # return render(request, "order-completed.html", {"order": order})

        return redirect("/processing-transaction")
        #return render(request, "processing-transaction.html", {"order": order})

    messages.warning(request, "Unable to place order. Please try again. ")
    return render(request, "process-mpesa.html", {"order": order})


def processing_transaction(request):
    cart = Cart(request)
    order_id = request.session.get("order_id")
    print('Order id' , order_id)

    for i in range(2):
        order = get_object_or_404(Order, id=order_id)
        if order.status == 'SUCCESSFUL':
            # mark the order as paid
            order.paid = True

            cart.clear()
            payment_completed.delay(order.id) #sends an email with invoice of payment

            messages.success(request, "Payment was successful")
            print("Payment successful", order.status)
            return render(request, "order-completed.html", {"order": order})
        elif order.status == 'Pending':

            #messages.warning(request, "Payment still pending")

            print("Payment still pending", order.status)
            time.sleep(2)
        else:
            messages.warning(request, "Payment failed")    
            print("Payment failed", order.status)
  
    return render(request, "processing-transaction.html", {"order": order})

    





def order_completed(request):
    return render(request, "order-completed.html")
   