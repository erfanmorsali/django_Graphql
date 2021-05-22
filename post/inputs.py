import graphene


class PostInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    description = graphene.String(required=True)
    category_id = graphene.Int(required=False)
