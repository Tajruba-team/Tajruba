from django.urls import path
from rest_framework import renderers
from knox import views as knox_views
from rest_auth.views import (
    LogoutView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)

from . import views
from .views import RegisterView, LoginView


account_list = views.AccountViewSet.as_view({
    'get': 'list'
})
account_detail = views.AccountViewSet.as_view({
    'get': 'retrieve'
})
account_profile = views.ProfileViewSet.as_view({
    'get': 'retrieve'
})

account_settings = views.settingsViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', account_list, name='account-list'),
    path('<int:pk>/', account_detail, name='account-detail'),

    path('<int:pk>/profile/', account_profile, name='account-profile'),
    path('<int:pk>/settings/', account_settings, name='account-settings'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logout-all'),

    # path('password/reset/', PasswordResetView.as_view(), name='rest-password'),
    # path('password/reset/confirm', PasswordResetConfirmView.as_view(), name='rest-password-confirm'),

    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/change/', PasswordChangeView.as_view(), name='password_change'),
]