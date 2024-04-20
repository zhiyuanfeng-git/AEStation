from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = 'dashboard/dashboard.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/profile.html'

class EventView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/event.html'

class FansView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/fans.html'