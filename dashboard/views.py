from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from rolepermissions.checkers import has_permission


class DashboardTemplateView(LoginRequiredMixin, TemplateView):
  login_url = reverse_lazy('login')
  template_name = 'dashboard/dashboard.html'

  def get(self, request):
    if (has_permission(request.user, 'manage_contribution')):
      return HttpResponseRedirect('/admin/contributions')

    return HttpResponseRedirect('/admin/contributions/create')


class SocialLoginTemplateView(TemplateView):
  template_name = 'dashboard/social.html'


class PrivacyPolicyTemplateView(TemplateView):
  template_name = 'dashboard/privacypolicy.html'
