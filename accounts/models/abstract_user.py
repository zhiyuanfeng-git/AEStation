from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser,AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
import uuid

from .manager import UserModelManager

DEFAULT_NAME_LENGTH = 150

class AbstractUserModel(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Email and password are required. Other fields are optional.
    """

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    username_validator = ASCIIUsernameValidator

    # manager
    objects = UserModelManager()

    # attributes
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=DEFAULT_NAME_LENGTH, blank=True)
    last_name = models.CharField(_('last name'), max_length=DEFAULT_NAME_LENGTH, blank=True)
    date_joined = models.DateTimeField(_('data joined'), default=timezone.now)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)    

    USERNAME_FIELD = 'email'

    # methods
    def cleanup(self):
        self.email = self.objects.normalize_email()

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()
    
    def get_short_name(self):
        return self.first_name
    
    def email_user(self, subject, message, from_email=None, **kwargs):
        """ Send an email to this user. """
        send_mail(subject, message, from_email, [self.email], **kwargs)