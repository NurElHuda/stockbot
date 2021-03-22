from django.db import models
from django.utils import timezone


class Product(models.Model):

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    name = models.CharField(max_length=1000, default="")

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if self.id:
            self.updated_at = timezone.now()
        return super(self.__class__, self).save(*args, **kwargs)
