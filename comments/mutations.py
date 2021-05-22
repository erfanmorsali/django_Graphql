from .inputs import CommentInput
import graphene
from .types import CommentType
from .models import Comment
from post.models import Post
from permissions.permissions import IsSuperUserPermission
from django_graphene_permissions import permissions_checker


class CreateComment(graphene.Mutation):
    class Arguments:
        input = CommentInput()

    ok = graphene.Boolean()
    comment = graphene.Field(CommentType)

    @permissions_checker([IsSuperUserPermission])
    def mutate(self, info, input=None):
        comment = Comment.objects.create(message=input.message)
        if input.posts:
            posts = []
            for post_id in input.posts:
                post = Post.objects.get(id=post_id)
                posts.append(post)
            comment.post.set(posts)
        ok = True
        return CreateComment(ok=ok, comment=comment)


class UpdateComment(graphene.Mutation):
    class Arguments:
        input = CommentInput()
        pk = graphene.Int()

    ok = graphene.Boolean()
    comment = graphene.Field(CommentType)

    @permissions_checker([IsSuperUserPermission])
    def mutate(self, info, pk, input=None):
        comment = Comment.objects.get(id=pk)
        comment.message = input.message
        if input.posts:
            post_list = []
            for post_id in input.posts:
                post = Post.objects.get(id=post_id)
                post_list.append(post)
            comment.post.set(post_list)
        comment.save()
        ok = True
        return UpdateComment(ok=ok, comment=comment)
