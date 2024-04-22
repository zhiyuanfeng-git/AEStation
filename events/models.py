import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
from fans.models import FansModel

UserModel = get_user_model()
# Create your models here.

class EventsModel(models.Model):

    # attributes
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField()
    event_url = models.SlugField(unique=True, blank=False, null=False)
    subscribers = models.ManyToManyField(FansModel, related_name='subscribed_events')

    def get_absolute_url(self):
        #return reverse('event-detail', args=[str(self.event_url)])
        #[TODO]
        return reverse('event-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.title