from django.db import models

from user.models import User


# Create your models here.
class Posts(models.Model):
    """
    stores the user posts
    """
    title: str = models.CharField(null=False, blank=False, max_length=128)
    content: str = models.CharField(null=False, blank=False, max_length=1024)
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    is_deleted: bool = models.BooleanField(null=False, default=False)
