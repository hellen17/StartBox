import email
from urllib import response
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny

from StartBx.apps.mpesa.models import Transaction
from StartBx.apps.orders.models import Order

from StartBx.apps.mpesa.utils import handle_stk_request
from . import serializers as sz

from django.contrib import messages
# Create your views here.
'''
Create ViewSet
Create Serializer
    -Model Fields
    - Validate phonenumber - check (ian_core) phonenumber
  
'''

class MpesaTransactionViewset(viewsets.ModelViewSet):
    serializer_class = None
    permission_classes = [AllowAny]

    queryset = Transaction.objects.all()


    def get_serializer_class(self):
        return sz.MpesaTransactionSerializer


    @action(detail=False, methods=['POST'], url_path='initiate')
    def initiate_stk(self,request):
        """
        Create a Transaction
        Send Requests to Remit API
        Listen for Transaction Status Updates

        """
        serializer = sz.MpesaTransactionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "error":True,
                "data":serializer.errors,
                "message":"Invalid Data"
            }, status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data
        phone_number = data.get('phone_number')
        amount = data.get('amount')
        reference = data.get('reference')
        # Create Transaction
        try:
            transaction = Transaction.objects.create(  
                phone_number=phone_number,
                amount=amount,
                reference=reference
            )
        except Exception as e: 
            return Response({
                "error":True,
                "data":data,
                "message":str(e)
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE) 

           
        #response = sz.MpesaDetailTransactionSerializer(transaction)
        '''
        If transaction is created, call Remit API
        Background Task to call Remit API using celery
        '''    
        #stk_response = handle_stk_request(data)
        r_status = handle_stk_request(phone_number, amount, reference)
        stk_response  = handle_stk_request(phone_number, amount, reference)

        print("Mpesa Response ", stk_response)
        print("R_status ", r_status)

        if r_status == True:
            Txndata = sz.MpesaDetailTransactionSerializer(transaction).data

            print("Response", Txndata)

            return Response(
                {
                    "success": True,
                    "data": Txndata,
                    "msg": "Payment request made, status is pending",
                },                    
                status=status.HTTP_200_OK
            )

        else:
            return Response(
                {
                    "error": True,
                    "data": "failedrequest",
                    "msg": "Something went wrong with your request. Try again later",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


      

    # @action(detail=False, methods=['POST'], url_path='status')  
    # def receive_callback(self,request):
    #     """
    #     Receive Callback from Remit API
    #     Update Transaction Status
    #     Test using Postman ngrok
    #     Get callback url for startbox .../mpesa/transactions/status
        
    #     """
    #     print(request.data)
    #     #webhook
    #     reference = request.data.get('reference') #reference should be unique
    #     trx: Transaction = Transaction.objects.get(reference=reference)
    #     trx.status = request.data.get('status') # sets status
    #     trx.save()
    #     return Response({ 
    #         "success":True,
    #     }, status=status.HTTP_200_OK) 


    @action(detail=False, methods=['POST'], url_path='status')  
    def receive_callback(self,request):
        """
        Receive Callback from Remit API
        Update Transaction Status
        Test using Postman ngrok
        Get callback url for startbox .../mpesa/transactions/status
        
        """
        
        print(request.data)
        body = request.data

        status = body['status']
        ian_reference = body['ian_reference']
        
        print("Status", status)

        if status == 'SUCCESSFUL':
            reference = request.data.get('reference') #reference should be unique

            #trx: Transaction = Transaction.objects.get(reference=reference)
            trx = Order.objects.get(id=reference)            
            trx.status = request.data.get('status') # sets status
          
            trx.mpesa_code = ian_reference
            trx.save()

            #messages.success(request, "Your order has been placed successfully")

            return Response({ 
                "success":True,
                "msg": "Callback successful",
                "data": trx.status


            })
        else:
            #messages.warning(request, "Your payment is still pending")
            return Response({ 
                "success":True,
                "msg": "Payment still pending"

            })  
           
  
        
    


