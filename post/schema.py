from graphene_django.types import ObjectType
import graphene
from .models import Post
from .types import PostType
from .mutations import CreatePost, UpdatePost, DeletePost


class PostQuery(ObjectType):
    post = graphene.Field(PostType, pk=graphene.Int())
    posts = graphene.List(PostType)

    @staticmethod
    def resolve_posts(self, info):
        return Post.objects.all()

    @staticmethod
    def resolve_post(self, info, pk):
        return Post.objects.filter(id=pk).first()


class PostMutate(ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()
