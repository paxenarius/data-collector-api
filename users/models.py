from django.db import models
from django.contrib.auth.models import AbstractUser
from contribution.models import Language
from otp.models import Pin
from otp.functions import generate_pin, send_message


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    default_language = models.ForeignKey(
        Language, default=None, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.username

    def get_pin(self):
        otps = self.pin_set.all()
        if otps:
            return otps.latest('created')
        else:
            return False

    def send_otp(self):
        otp = generate_pin()
        send_message(self.username, otp)
        self.pin_set.create(pin=otp)
        return True

