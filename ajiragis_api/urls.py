"""ajiragis_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from dashboard.views import DashboardTemplateView, SocialLoginTemplateView, PrivacyPolicyTemplateView

urlpatterns = [
    path('data-collector/', SocialLoginTemplateView.as_view(), name='social'),
    path('data-collector/privacypolicy/', PrivacyPolicyTemplateView.as_view(), name='privacypolicy'),
    path('data-collector/admin/', admin.site.urls),
    path('data-collector/accounts/login/', SocialLoginTemplateView.as_view(), name='signup'),
    path('data-collector/accounts/', include('allauth.urls')),
    path('data-collector/contributions/', include('contribution.urls')),
    path('data-collector/dashboard/', DashboardTemplateView.as_view(), name='dashboard'),
    path('data-collector/api/v1/', include('api.urls')),
    path('data-collector/users/', include('users.urls')),
    path('data-collector/users/', include('django.contrib.auth.urls')),
    path('data-collector/otp/', include('otp.urls')),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
