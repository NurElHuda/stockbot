from django.db import models
from django.utils import timezone


class Admin(models.Model):

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    user = models.OneToOneField(
        "api.User",
        on_delete=models.CASCADE,
        related_name="admin",
    )

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if self.id:
            self.updated_at = timezone.now()
        else:
            self.user.is_admin = True
        return super(self.__class__, self).save(*args, **kwargs)
