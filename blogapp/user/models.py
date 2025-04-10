from django.db import models


# Create your models here.
class User(models.Model):
    """
    represents the user table in db
    """
    username: str = models.CharField(null=False, max_length=50)
    email: str = models.CharField(null=False, max_length=256)
    about: str = models.CharField(max_length=1024)
    password: str = models.CharField(max_length=60)
    is_deleted: bool = models.BooleanField(default=False, null=False)
