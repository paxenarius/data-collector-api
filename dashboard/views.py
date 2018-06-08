from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'


class SocialLoginTemplateView(TemplateView):
    template_name = 'dashboard/social.html'


class PrivacyPolicyTemplateView(TemplateView):
    template_name = 'dashboard/privacypolicy.html'
