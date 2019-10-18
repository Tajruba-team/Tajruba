from django.urls import path
from rest_framework import renderers

from . import views
from .views import RegisterView


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
]