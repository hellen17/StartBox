from celery import shared_task

from django.core.mail import send_mail

from StartBx.apps.mpesa.utils import handle_stk_request
from .models import Order

@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    print(order.id,order.phone_number,order.get_total_cost())

    '''Call STK Push function(moved this to a separate view)'''

    # response = handle_stk_request(phone_number=order.phone_number,amount=str(order.get_total_cost()),reference=order.id)

    # print("Response is:", response)

    

    subject = f'We await your payment for Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'hellen@impactafrica.network',
                          [order.email])
    return mail_sent

#shalom.nyende@gmail.com