from django.urls import path
from .views import HomeView, AboutView, DashboardView, ProfileView, EventView, FansView
from .views import test
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('event/', EventView.as_view(), name='event'),
    path('fans/', FansView.as_view(), name='fans'),
]