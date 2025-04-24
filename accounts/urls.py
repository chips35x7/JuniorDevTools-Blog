from django.urls import path

from .views import *


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('account_delete', AccountDeleteView.as_view(), name='account_delete'),
    path('account_deactivate', AccountDeactivateView.as_view(), name='account_deactivate')
    ]