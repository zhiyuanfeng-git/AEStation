from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EventsForm
from .models import EventsModel
from django.urls import reverse_lazy

# Create your views here.

class EventView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/event.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["created_event"] = self.request.user.eventsmodel_set.all()
        return context

class CreateEventView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/event_create.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        form = EventsForm()
        context["form"] = form
        return context
    
    def post(self, request, *args, **kwargs):
        user = request.user
        form = EventsForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = user
            event.save()
            return redirect(event)
        else:
            context = self.get_context_data(form=form)
            return self.render_to_response(context)
        
class EventDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/event_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_url = self.kwargs['pk']
        event = get_object_or_404(EventsModel, pk=event_url)
        context['event'] = event
        return context