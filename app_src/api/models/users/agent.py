from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_lifecycle import hook
from django_lifecycle.hooks import AFTER_CREATE
from django_lifecycle.mixins import LifecycleModelMixin


class Agent(LifecycleModelMixin, models.Model):

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    user = models.OneToOneField(
        "api.User",
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="agent",
    )

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if self.id:
            self.updated_at = timezone.now()
        return super(self.__class__, self).save(*args, **kwargs)

