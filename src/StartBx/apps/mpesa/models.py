from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from dataclasses import dataclass


# Create your models here.
"""
1. Create a Transaction Model
 - ID, Timestamp, Amount, Phone Number, Account number, Transaction status
2. Crete view/util to call MPESA API (Living under api.pokea.co)
3. Initiate Transaction (C2B via STK Push)
4. Listen for Transaction Status Updates

"""


@dataclass
class TxnStatus:
    PENDING: str = "Pending"
    SUCCESS: str = "Success"
    FAILED: str = "Failure"

class Transaction(models.Model):
    '''Transaction Model'''
    id = models.BigAutoField(primary_key=True, unique=True)
    timestamp = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=30, default='Pending')
    phone_number = models.CharField(max_length=30)
    reference = models.CharField(max_length=30, default=TxnStatus.PENDING)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    


    def __str__(self):
        return f"{self.id} - {self.timestamp} - {self.amount} - {self.status}"
