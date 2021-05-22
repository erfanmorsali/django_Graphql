from django.db import models
from post.models import Post


# Create your models here.

class Comment(models.Model):
    """"
    Relation Between Post And Comment is OneToMany..But Just For Test ManyToMany In Graphql
    """
    post = models.ManyToManyField(Post, blank=True, related_name="comments")
    message = models.TextField()

    def __str__(self):
        return self.message
