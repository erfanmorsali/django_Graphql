import graphene


class CategoryInput(graphene.InputObjectType):
    name = graphene.String(required=True)
