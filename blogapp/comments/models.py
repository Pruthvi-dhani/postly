from __future__ import annotations

from django.db import models

from user.models import User
from posts.models import Posts


# Create your models here.
class Comments(models.Model):
    """
    stores user comments on posts
    """
    comment: str = models.CharField(null=False, blank=False, max_length=512)
    is_deleted: bool = models.BooleanField(null=False, default=False)
    parent_comment: Comments = models.ForeignKey("self", null=True, blank=False, on_delete=models.CASCADE,
                                                 related_name="child_comments")
    user: User = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post: Posts = models.ForeignKey(Posts, null=False, blank=False, on_delete=models.CASCADE)
