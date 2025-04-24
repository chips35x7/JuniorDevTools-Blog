from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('settings', SettingsView.as_view(), name='settings'),
    path('update_username', UpdateUsernameView.as_view(), name='update_username'),
    path('update_email', UpdateEmailView.as_view(), name='update_email'),
    path('update_f.name', UpdateFirstNameView.as_view(), name='update_f_name'),
    path('update_l.name', UpdateLastNameView.as_view(), name='update_l_name'),
    path('update_m_name', UpdateMiddleNameView.as_view(), name='update_m_name'),
    path('update_profile_pic', UpdateProfilePicView.as_view(), name='update_profile_pic'),
]