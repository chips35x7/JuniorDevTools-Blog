from django.views.generic import TemplateView, FormView, View
from django.views.generic.edit import UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from accounts.views import AccountPrivacyView

from .forms import FeedBackForm

USER_MODEL = get_user_model()


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(FormView):
    template_name = 'pages/about.html'
    form_class = FeedBackForm
    success_url = reverse_lazy('about')

    def form_valid(self, form):
        feedback = form.save(commit=False)
        feedback.user = self.request.user
        feedback.save()
        return super().form_valid(form)


class SettingsView(LoginRequiredMixin, View):
    template_name = 'pages/profile_settings/profile_settings.html'

    def get(self, request, *args, **kwargs):
        view = AccountPrivacyView.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = AccountPrivacyView.as_view()
        return view(request, *args, **kwargs)


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