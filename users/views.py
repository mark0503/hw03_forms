from django.contrib.auth.views import SuccessURLAllowedHostsMixin, PasswordContextMixin
from django.shortcuts import render
from django.views.generic import CreateView, FormView, TemplateView
from django.urls import reverse_lazy
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('signup')
    template_name = 'signup.html'
# Create your views here.


class LoginView(SuccessURLAllowedHostsMixin, FormView):
    template_name = 'registration/login.html'


class LogoutView(SuccessURLAllowedHostsMixin, TemplateView):
    template_name = 'registration/logged_out.html'


class PasswordResetView(PasswordContextMixin, FormView):
    template_name = 'registration/password_reset_form.html'


class PasswordResetDoneView(PasswordContextMixin, TemplateView):
    template_name = 'registration/password_reset_done.html'


class PasswordResetConfirmView(PasswordContextMixin, FormView):
    template_name = 'registration/password_reset_confirm.html'


class PasswordResetCompleteView(PasswordContextMixin, TemplateView):
    template_name = 'registration/password_reset_complete.html'


class PasswordChangeView(PasswordContextMixin, FormView):
    template_name = 'registration/password_change_form.html'


class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    template_name = 'registration/password_change_done.html'
