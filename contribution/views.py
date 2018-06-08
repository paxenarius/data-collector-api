from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from rest_framework import viewsets

from contribution.models import Data, Language
from contribution.serializers import LanguageSerializer, ContributionSerializer


class ContributionCreateView(LoginRequiredMixin, CreateView):
    model = Data
    fields = ['language', 'text', 'file']
    template_name = 'contribution/contribution_create.html'
    success_url = reverse_lazy('contribute-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ContributionListView(LoginRequiredMixin, ListView):
    model = Data
    template_name = 'contribution/contribution_list.html'


class LanguageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class ContributionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Data.objects.all()
    serializer_class = ContributionSerializer