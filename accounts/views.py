from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import UserSignUpForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect

USER_MODEL = get_user_model()


class SignUpView(CreateView):
    form_class = UserSignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user=user)
        return redirect(self.success_url)


class AccountDeactivateView(LoginRequiredMixin, UpdateView):
    model = USER_MODEL
    fields = ('is_active',)
    template_name = 'registration/account_deactivate.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset = None):
        obj = get_object_or_404(USER_MODEL, pk=self.request.user.pk, username=self.request.user.username)
        return obj
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        form.save()
        return super().form_valid(form)
    

class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = USER_MODEL
    template_name = 'registration/account_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset = None):
        obj = get_object_or_404(USER_MODEL, pk=self.request.user.pk, username=self.request.user.username)
        return obj