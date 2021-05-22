from category.models import Category
from graphene_django.types import DjangoObjectType


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
