from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from guardian.mixins import GuardianUserMixin
from django.core.mail import send_mail
from django.db import models


from .managers import UserManager


class User(AbstractBaseUser, GuardianUserMixin, PermissionsMixin):
    netid = models.CharField("net id", max_length=30, unique=True)
    email = models.EmailField("email address", blank=True, null=True)
    first_name = models.CharField("first name", max_length=30, blank=True)
    last_name = models.CharField("last name", max_length=30, blank=True)
    date_joined = models.DateTimeField("date joined", auto_now_add=True)
    is_active = models.BooleanField("active", default=True)
    is_staff = models.BooleanField("staff status", default=False)
    is_superuser = models.BooleanField("superuser status", default=False)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "netid"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.netid

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        if self.email is not None:
            send_mail(subject, message, from_email, [self.email], **kwargs)
