from graphene.types import InputObjectType
import graphene


class CommentInput(InputObjectType):
    message = graphene.String(required=True)
    posts = graphene.List(graphene.Int, required=False)
