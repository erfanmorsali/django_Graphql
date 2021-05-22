import graphene
from graphene_django.types import ObjectType
from .types import CommentType
from .models import Comment
from .mutations import CreateComment, UpdateComment


class CommentQuery(ObjectType):
    comments = graphene.List(CommentType)
    comment = graphene.Field(CommentType, pk=graphene.Int())

    @staticmethod
    def resolve_comments(self, info):
        return Comment.objects.all()

    @staticmethod
    def resolve_comment(self, info, pk):
        return Comment.objects.get(id=pk)


class CommentMutate(ObjectType):
    create_comment = CreateComment.Field()
    update_comment = UpdateComment.Field()
