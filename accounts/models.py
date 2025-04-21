from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Users(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    # profile_picture = models.ImageField(default='fallback.png', upload_to='user_profile_pic/', blank=True)