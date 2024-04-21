from django.shortcuts import redirect
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

    def _update_name(self, user, first_name, last_name):
        updated = False
        if first_name:
            user.first_name = first_name
            updated = True
        if last_name:
            user.last_name = last_name
            updated = True
        
        if updated:
            user.save()

    def post(self, request, *args, **kwargs):
        user = request.user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        self._update_name(user, first_name, last_name)

        return redirect('profile')


class EventView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/event.html'

class FansView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/fans.html'