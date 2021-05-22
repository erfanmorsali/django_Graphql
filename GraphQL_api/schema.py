import graphene
from post.schema import PostQuery, PostMutate
from category.schema import CategoryQuery, CategoryMutate
from comments.schema import CommentQuery, CommentMutate
import graphql_jwt


class Query(CommentQuery, CategoryQuery, PostQuery, graphene.ObjectType):
    pass


class Mutate(CommentMutate, CategoryMutate, PostMutate, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutate)
