import requests

def handle_stk_request(data):

    """
    Handle STK Push Requests

    1. Call Remit API
    2. Listen for Transaction Status Updates
    3. Update Transaction Status

    """
    # Get Data from Request

    TILL_NO = '5002' #TODO: Register for till number from IAN Remit
    payload = {
        "till_number":TILL_NO,
        "request_amount":data.get('amount'),
        "reference":data.get('reference'),
        "sender_phone":data.get('phone_number'),
    }
    URL = 'https://api.pokea.co/transactions/mobile-money/stk/'

    '''
    Fill in this details with your details from IAN REMIT API
    '''
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'khtruehteo',
        'X-IDT': 'A',
        'MID': '21',
        'XAT':'M'
    }
    r = requests.post(URL, data=payload, headers=headers)
    print(r.json())
    return payload