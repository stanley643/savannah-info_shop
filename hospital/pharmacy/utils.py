import africastalking
from .models import Order
from hospital import settings
from django.conf import settings

def send_sms(recipient, message):
    africastalking.initialize(username=settings.AFRICASTALKING_USERNAME, api_key=settings.AFRICASTALKING_API_KEY)
    sms = africastalking.SMS
    sms.send([recipient], message)