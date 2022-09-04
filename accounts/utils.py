import os

from decouple import config
from twilio.rest import Client

account_sid='AC7bde225e66cbfcacbfe23b1cf92b996b'
auth_token='27823cc91ddb431666d0cef5a9d93903'

client = Client(account_sid,auth_token)

def send_sms(user_code,phone_number):
    message = client.messages.create(
        body = f'Hi! Your OTP verification code is {user_code}',
        from_='+12245019525',
        to = f'{phone_number}'

    )
    # print(message.sid)
    return send_sms