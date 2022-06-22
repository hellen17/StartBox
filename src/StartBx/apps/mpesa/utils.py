from redis import ResponseError
from decouple import config

import requests

# def handle_stk_request(amount,phone_number,reference):

#     """
#     Handle STK Push Requests

#     1. Call Remit API
#     2. Listen for Transaction Status Updates
#     3. Update Transaction Status

#     """
#     # Get Data from Request

#     TILL_NO = '5002' #TODO: Register for till number from IAN Remit
#     payload = {
#         "till_number":TILL_NO,
#         "request_amount":amount,
#         "reference":reference,
#         "sender_phone":phone_number,
#     }
#     URL = 'https://api.pokea.co/transactions/mobile-money/stk/'

#     '''
#     Fill in this details with your details from IAN REMIT API
#     '''
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': 'khtruehteo',
#         'X-IDT': 'A',
#         'MID': '21',
#         'XAT':'M'
#     }
#     r = requests.post(URL, json=payload, headers=headers)
#     print(r.json())
#     return payload

def getAccessToken():
    headers = {
        'Content-Type': 'application/json',
        'X-IDT': "A",
    }
    
    payload = {
        "email": config('IAN_REMIT_EMAIL'),
        "password": config('IAN_REMIT_PASS')
    }

    try:
        response = requests.request("POST", config('IAN_REMIT_URL') + '/accounts/auth/signin/', headers = headers, json=payload)
        if response.status_code==200:
            body = response.json()
            access_key = body['data']['token']
            return True, access_key
        else:
            return False, response.json()
    except Exception as e:
        return False, e


def handle_stk_request(phone_number, amount, reference):
    status, access_key = getAccessToken()
    print("Access key:", access_key)
    
    first = phone_number[0]
    if first == "+":
        phone_number = phone_number[1:]



    if status == True:
        headers = {
            'Content-Type': 'application/json',
            'X-IDT': 'A',
            'XAT': "M",
            'Authorization': access_key,
        }

        till_number = 5004
  
        payload = {
            "till_number": till_number,
            "request_amount": amount,
            "reference": f'STARTBX{reference}',
            "sender_phone": phone_number
        }

        print('Payload:')
        print(payload)

        try:
            response = requests.request("POST", config('IAN_REMIT_URL') + '/transactions/mobile-money/stk/', headers = headers, json = payload)
         
            print("Status:", response.status_code)
            response_json = response.json()

            if response.status_code == 202: #checks if the request was accepted for processing
                print('Mpesa Request Pass', response.json())
                return True, response_json
            else:
                return False, response_json
        except Exception as e:
            print(str(e))
            print('Mpesa Request Fail')
#         
    else:
        return False, "Something went wrong when communicating with Mpesa"





# "gAAAAABiqhsbgTazSwe14r4Nukds6_4w-hqGuau4F0CqkZNjvV5s9yGkE50y1eN40CR7OqqblVWPplNFDFDZKpig8KH2zJaPT2z421pQ36YwQvdy2HrQbTwLqzMaNluc_lkx4gN2YJccTSk1BfdP6HJfxhmLMAI1frxzpv-sfOclc686Pdk2TIr7fn0rRa1rmy8qTelFl2ashhp74fFPSBmT8m-ZML_0MbFo_N9dQHd1KCYgwRJrSoL2e_l0-EErs1yLK0IWoWow47zvX6wMWJaH0gt4EUVEMwT9exmuda8PliL-3eQZGblHGkT11XxEbY8w8XounxLamVwGWUiec4SyjGj2qAxahA=="
TOKEN = "gAAAAABiqx-KJz2G-tvLNFbjTLv0PFlmBFbamQ7tr4SjMuo5i2mxuLzdG9zK237e7LNXCcjWG4lNpd96zsQEuOScbZ1ElroZZiHePiqq1CaZK1-ceRSfB9o0nDam9SvZky2gg7WfU9JnNW0W91cbttZeKricaU0kgg5jRdc4H8drFcDr-jo3a1SdtvCUTyZJjQqwFa5JH1KON_fUfSOYmL3lkDmPub2VLlLERgkKdnr7PT9FndC9bOM_EY5t-V6SyPRQcEu9eCsbNxa8-56c8HrNYag_tPnELhIGaLK9OkeIfM7bsCTz-kID2na24or3kFxgPfoxVcElmYffFHxrLhiVv024zu-Yhw=="

# def handle_stk_request(phone_number, amount, reference):
#     access_key = getAccessToken()

#     first = phone_number[0]
#     if first == "+":
#         phone_number = phone_number[1:]
#     payload = {
#         "till_number": "5002",
#         "request_amount": amount,
#         "reference": reference,
#         "phone_number": phone_number,
#     }
        
#     print('Payload:')
#     print(payload)
#     try:
#         r = requests.post(
#             "https://api.pokea.co/transactions/mobile-money/stk/",
#             headers={
#                 'Content-Type': 'application/json',
#                 'X-IDT': 'A',
#                 'XAT': "M",
#                 'Authorization': access_key,
#             },
#             json=payload,
#         )
#         print("Status Code:", r.status_code)
#         print(r.json())
#         return payload
#     except Exception as e:
#         print(str(e))
#         print('Mpesa Request Failed')

        