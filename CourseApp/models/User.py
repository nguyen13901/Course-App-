from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='upload/%Y/%m')

    class Meta:
        db_table = "user"
