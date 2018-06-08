from django.urls import path

from contribution.views import ContributionListView, ContributionCreateView
from dashboard.views import PrivacyPolicyTemplateView

urlpatterns = [
    path('', ContributionListView.as_view(), name='contribute-list'),
    path('create/', ContributionCreateView.as_view(), name='contribute-create'),
    path('privacypolicy/', PrivacyPolicyTemplateView.as_view(), name='privacypolicy'),
]
