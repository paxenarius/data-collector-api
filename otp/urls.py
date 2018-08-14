from django.urls import include, path
from .views import OtpTemplateView, otp_view

urlpatterns = [
    path('', otp_view, name='otp'),
]