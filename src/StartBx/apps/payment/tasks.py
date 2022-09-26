from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from StartBx.apps.orders.models import Order
from StartBx.apps.frontend.models import Product,Packages
from StartBx.settings.aws.config import MEDIA_ROOT

import requests

@shared_task
def payment_completed(order_id, product_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    #fetch id of current product
    product = Product.objects.get(id=product_id)
    print('product is', product)
    files = product.product_items.all() 
    print('file is', files)
    # guide_name = files.filter(product_id=product_id)
    # print('guide is', guide_name[0].guide)


    print('Media root is', MEDIA_ROOT)
    product_pdf = product.file.name
    print('product_pdf path',product_pdf)

    # MEDIA_URL = f'//{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/' 
    # MEDIA_ROOT = MEDIA_URL
    test = f'https:{MEDIA_ROOT}{product_pdf}'
    print('test', test)
    # create invoice e-mail
    subject = f"StartBox - EE Invoice no. {order.id}"

    message = "Please, find attached your template and the invoice for your recent purchase."
    email = EmailMessage(subject, message, "hellen@impactafrica.network", [order.email])

    # generate PDF
    html = render_to_string("orders/order/pdf.html", {"order": order})
    out = BytesIO()
    weasyprint.HTML(string=html).write_pdf(out)

    response = requests.get(f'https:{MEDIA_ROOT}{product_pdf}')
    print('response', response)

    # attach PDF file
    email.attach(f"order_{order.id}.pdf", out.getvalue(), "application/pdf")
    email.attach(product_pdf, response.content,mimetype="application/pdf")

    # send multiple documents
    for i in files:
        list = i.guide
        path = f'https:{MEDIA_ROOT}{list}'
        guide_response = requests.get(path)
        print('guide_response', guide_response)
        email.attach(f'{i.guide}', guide_response.content, 'application/pdf')


    # email.attach_file(f'https:{MEDIA_ROOT}{product_pdf}', "application/pdf")
    # email.attach_file('/home/hellen/Documents/projects/IAN/StartBx/src/StartBx/templates/documents/NDA.pdf')

    # send e-mail
    email.send()
