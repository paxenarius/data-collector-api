from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from contribution.views import LanguageViewSet, ContributionViewSet
from users.views import CustomUserListView

router = routers.DefaultRouter()
router.register(r'languages', LanguageViewSet)
router.register(r'users', CustomUserListView)
router.register(r'contributions', ContributionViewSet)

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]