from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from contribution.models import Data


class DashboardTemplateView(TemplateView):
    template_name = 'dashboard/dashboard.html'


class SocialLoginTemplateView(TemplateView):
    template_name = 'dashboard/social.html'
