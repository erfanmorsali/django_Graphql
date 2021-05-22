from graphene_django.types import ObjectType
import graphene
from .types import CategoryType
from .models import Category
from .mutations import CreateCategory, UpdateCategory


class CategoryQuery(ObjectType):
    category = graphene.Field(CategoryType, pk=graphene.Int())

    categories = graphene.List(CategoryType)

    @staticmethod
    def resolve_categories(self, info):
        return Category.objects.all()

    @staticmethod
    def resolve_category(self, info, pk):
        return Category.objects.filter(id=pk).first()


class CategoryMutate(ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
