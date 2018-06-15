from django.urls import path

from contribution.views import ContributionListView, ContributionCreateView, ContributionApprovalView
from dashboard.views import PrivacyPolicyTemplateView

urlpatterns = [
    path('', ContributionListView.as_view(), name='contribute-list'),
    path('create/', ContributionCreateView.as_view(), name='contribute-create'),
    path('approve/<pk>/', ContributionApprovalView.as_view(), name='contribute-approve')
]
