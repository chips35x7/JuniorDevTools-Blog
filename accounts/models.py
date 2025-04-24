from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Users(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    profile_picture = models.ImageField(default='fallback.png', upload_to='user_profile_pictures/', blank=True)