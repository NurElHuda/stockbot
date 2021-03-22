from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import DateField
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_lifecycle import LifecycleModelMixin, hook
from django_lifecycle.hooks import BEFORE_SAVE
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class User(AbstractUser, LifecycleModelMixin):

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    USER_TYPE = [
        ("Admin", "Admin"),
        ("Manager", "Manager"),
        ("Agent", "Agent"),
    ]

    name = models.CharField(blank=True, max_length=255, default="")
    email = models.EmailField(max_length=255, unique=True)
    birthday = DateField(default=None, null=True, blank=True)
    picture = ProcessedImageField(
        max_length=1000,
        upload_to="users/images",
        processors=[ResizeToFill(413, 531)],
        format="JPEG",
        options={"quality": 85},
        null=True,
    )

    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if self.id:
            self.updated_at = timezone.now()
        return super(self.__class__, self).save(*args, **kwargs)

    def __str__(self):
        return self.pk + " | " + self.name

    @property
    def user_type(self):
        if self.is_admin:
            return "admin"
        elif self.is_manager:
            return "manager"
        elif self.is_manager:
            return "agent"
        else:
            return "unknown"


def create_user(user_validated_data):
    password = user_validated_data.pop("password", False)
    user = User.objects.create(**user_validated_data)

    if password:
        user.set_password(password)
    user.save()
    return user


def update_user(user, validated_data):
    if validated_data.get("password", False):
        user.set_password(validated_data.get("password"))

    for key, value in validated_data.items():
        setattr(user, key, value)

    user.save()
    return user