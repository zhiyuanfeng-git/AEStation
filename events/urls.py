from django.urls import path
from .views import EventView, CreateEventView, EventDetailView

urlpatterns = [
    path('event/', EventView.as_view(), name='event'),
    path('create/', CreateEventView.as_view(), name='create-event'),
    path('events/<pk>/', EventDetailView.as_view(), name='event-detail'),
]