from django.db import models

from user.models import User
from posts.models import Posts
from comments.models import Comments


# Create your models here.
class PostLikes(models.Model):
    """
    user likes to a post
    """
    user: User = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post: Posts = models.ForeignKey(Posts, null=False, blank=False, on_delete=models.CASCADE)
    is_deleted: bool = models.BooleanField(null=False, default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "post"], name="postlikes_user_id_post_id_unique_constraint")
        ]


class CommentLikes(models.Model):
    """
    user likes to a comment
    """
    user: User = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    comment: Comments = models.ForeignKey(Comments, null=False, blank=False, on_delete=models.CASCADE)
    is_deleted: bool = models.BooleanField(null=False, default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "comment"],
                                    name="commentlikes_user_id_comment_id_unique_constraint")
        ]
