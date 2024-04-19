from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserModelCreationForm

# Create your views here.

class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserModelCreationForm
    success_url = reverse_lazy("login")