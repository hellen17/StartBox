"""
Identify the flow of operations/business rules

Model

Create serializer
Create viewset(Basic one with skeleton view)
Create URL conf
Register URL conf with root Url conf
Acknowledgement from endpoint

"""
from rest_framework import serializers
from StartBx.apps.mpesa.models import Transaction
import phonenumbers

class MpesaTransactionSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=30)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    reference = serializers.CharField(max_length=30)

    # def validate(self,attrs):
    #     if not attrs['phone_number'].startswith('254'):
    #         raise serializers.ValidationError("Invalid Phone Number")
    #     return attrs

    def validate(self, attrs):
        try:
            phone_number = "+" + str(int(attrs["phone_number"])).replace(" ", "")
            x = phonenumbers.parse(phone_number, None)
        except Exception as e:
            raise serializers.ValidationError("Please enter a valid phone number")
        if not phonenumbers.is_valid_number(x):
            raise serializers.ValidationError(f"Invalid phone number {phone_number}")
        attrs["phone"] = str(int(phone_number))
        return attrs


class MpesaDetailTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'    