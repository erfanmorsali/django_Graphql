import graphene
from .inputs import CategoryInput
from .types import CategoryType
from .models import Category
from permissions.permissions import IsSuperUserPermission
from django_graphene_permissions import permissions_checker


class CreateCategory(graphene.Mutation):
    class Arguments:
        input = CategoryInput()

    category = graphene.Field(CategoryType)

    @permissions_checker([IsSuperUserPermission], )
    def mutate(self, info, input=None):
        category = Category.objects.create(name=input.name)
        return CreateCategory(category=category)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        input = CategoryInput()
        pk = graphene.Int()

    category = graphene.Field(CategoryType)

    @permissions_checker([IsSuperUserPermission])
    def mutate(self, info, pk, input=None):
        category = Category.objects.get(id=pk)
        category.name = input.name
        category.save()
        return UpdateCategory(category=category)
