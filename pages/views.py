from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


USER_MODEL = get_user_model()


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/profile_settings/profile_settings.html'


class UpdateUsernameView(LoginRequiredMixin, UpdateView):
    model = USER_MODEL
    fields = ('username',)
    template_name = 'pages/profile_settings/update_username.html'
    success_url = reverse_lazy('settings')

    def get_object(self, queryset = None):
        obj = get_object_or_404(USER_MODEL, pk=self.request.user.pk, username=self.request.user.username)
        return obj

class UpdateEmailView(LoginRequiredMixin, UpdateView):
    model = USER_MODEL
    fields = ('email',)
    template_name = 'pages/profile_settings/update_email.html'
    success_url = reverse_lazy('settings')
    
    def get_object(self, queryset = None):
        obj = get_object_or_404(USER_MODEL, pk=self.request.user.pk, username=self.request.user.username)
        return obj
    

class UpdateFirstNameView(LoginRequiredMixin, UpdateView):
    model = USER_MODEL
    fields = ('first_name',)
    template_name = 'pages/profile_settings/update_f_name.html'
    success_url = reverse_lazy('settings')
    
    def get_object(self, queryset = None):
        obj = get_object_or_404(USER_MODEL, pk=self.request.user.pk, username=self.request.user.username)
        return obj
    

class UpdateLastNameView(LoginRequiredMixin, UpdateView):
    model = USER_MODEL
    fields = ('last_name',)
    template_name = 'pages/profile_settings/update_l_name.html'
    success_url = reverse_lazy('settings')
    
    def get_object(self, queryset = None):
        obj = get_object_or_404(USER_MODEL, pk=self.request.user.pk, username=self.request.user.username)
        return obj
    

class UpdateMiddleNameView(LoginRequiredMixin, UpdateView):
    model = USER_MODEL
    fields = ('middle_name',)
    template_name = 'pages/profile_settings/update_m_name.html'
    success_url = reverse_lazy('settings')
    
    def get_object(self, queryset = None):
        obj = get_object_or_404(USER_MODEL, pk=self.request.user.pk, username=self.request.user.username)
        return obj
    

class UpdateProfilePicView(LoginRequiredMixin, UpdateView):
    model = USER_MODEL
    fields = ('profile_picture',)
    template_name = 'pages/profile_settings/update_profile_pic.html'
    success_url = reverse_lazy('settings')

    def get_object(self, queryset = None):
        obj = get_object_or_404(USER_MODEL, pk=self.request.user.pk, username=self.request.user.username)
        return obj