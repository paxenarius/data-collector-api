from django.urls import path

from contribution.views import ContributionListView, ContributionCreateView

urlpatterns = [
    path('', ContributionListView.as_view(), name='contribute-list'),
    path('create/', ContributionCreateView.as_view(), name='contribute-create'),

]
