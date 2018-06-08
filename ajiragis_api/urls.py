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
from django.contrib import admin
from django.urls import path, include
from dashboard.views import DashboardTemplateView, SocialLoginTemplateView, PrivacyPolicyTemplateView

urlpatterns = [
    path('', SocialLoginTemplateView.as_view(), name='social'),
    path('privacypolicy/', PrivacyPolicyTemplateView.as_view(), name='privacypolicy'),
    path('admin/', admin.site.urls),
    path('accounts/login/', SocialLoginTemplateView.as_view(), name='signup'),
    path('accounts/', include('allauth.urls')),
    path('contributions/', include('contribution.urls')),
    path('dashboard/', DashboardTemplateView.as_view(), name='dashboard'),
    path('api/v1/', include('api.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
