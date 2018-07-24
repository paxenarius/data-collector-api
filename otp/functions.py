import random
import string

import africastalking
from django.conf import settings


USERNAME = 'ajiragis'
API_KEY = '6d9e2a0e201a8baa4c80d803c4ec9d2b350b72be8b44c78e2e9a36d17fe650d2'


def generate_pin(length=6):
    ''' generate an OTP '''
    chars = string.digits
    otp = ''
    for i in range(length):
        otp += chars[int(random.random() * 10)]
    return int(otp)


def send_message(phone_number, otp):
    ''' send a message with the otp'''
    africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)
    sms = africastalking.SMS
    phone_number = '+254' + str(phone_number)[1:]
    message = 'Use this PIN to login to Ajira : {}'.format(str(otp))
    response = sms.send(message, [phone_number])
    try:
        status = response['SMSMessageData']['Recipients'][0]['status']
        if status == 'Success':
            return {
                'phone_number': phone_number,
                'otp': otp
            }
        return False
    except Exception as e:
        print(e)
        return False


# if __name__ == '__main__':
#     otp = generate_pin()
#     sent = send_message('0721217172', otp)
#     print (sent)
