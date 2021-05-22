import graphene
from django_graphene_permissions import permissions_checker
from category.models import Category
from .inputs import PostInput
from .types import PostType
from .models import Post
from permissions.permissions import IsSuperUserPermission


class CreatePost(graphene.Mutation):
    class Arguments:
        input = PostInput()

    post = graphene.Field(PostType)

    @permissions_checker([IsSuperUserPermission])
    def mutate(self, info, input=None):
        input_data = dict(input)
        category_id = input_data.pop("category_id")
        category = Category.objects.get(id=category_id)
        post = Post.objects.create(category=category, **input_data)
        return CreatePost(post=post)


class UpdatePost(graphene.Mutation):
    class Arguments:
        input = PostInput()
        pk = graphene.Int()

    post = graphene.Field(PostType)

    @permissions_checker([IsSuperUserPermission])
    def mutate(self, info, pk, input=None):
        data = dict(input)
        post = Post.objects.filter(id=pk)
        post.update(**data)
        return UpdatePost(post=post.first())


class DeletePost(graphene.Mutation):
    class Arguments:
        pk = graphene.Int()

    ok = graphene.Boolean()

    @permissions_checker([IsSuperUserPermission])
    def mutate(self, info, pk):
        post = Post.objects.get(id=pk)
        post.delete()
        ok = True
        return DeletePost(ok=ok)
