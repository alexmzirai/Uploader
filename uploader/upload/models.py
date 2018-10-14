from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import datetime


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)   # associate a profile to a user
    location = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='pictures')

    class Meta:
        db_table = 'profile'
        verbose_name_plural = "Profiles"
        ordering = ['location']







