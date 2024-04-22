import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()

# Create your models here.
DEFAULT_NAME_LENGTH = 150

class FansModel(models.Model):

    # attributes
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=DEFAULT_NAME_LENGTH)
    middle_name = models.CharField(max_length=DEFAULT_NAME_LENGTH, blank=True)
    last_name = models.CharField(max_length=DEFAULT_NAME_LENGTH, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    owners = models.ManyToManyField(UserModel, related_name='owners_fans')

    def __str__(self):
        return f"{self.first_name}#{self.email}"