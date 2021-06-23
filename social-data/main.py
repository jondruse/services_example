from ariadne import gql, QueryType
from ariadne.constants import PLAYGROUND_HTML
from ariadne.contrib.federation import FederatedObjectType, make_federated_schema
from ariadne.asgi import GraphQL
import uvicorn

type_defs = gql("""
  type Query {
      social_data: [SocialData]
  }

  type SocialData @key(fields:"email") {
    email: String!   
    phone: String
    avatar_url: String
    twitter_url: String
    facebook_url: String
    user: User! @provides(fields:"email")
  }

  type User @key(fields: "email") @extends {
    id: ID! @external
    email: String! @external
    social_data: SocialData
  }
""")

query = QueryType()
user = FederatedObjectType("User")
social_data = FederatedObjectType("SocialData")

@query.field("social_data")
def resolve_social_data(*_):
    return mock_social_data

@social_data.reference_resolver
def resolve_social_data_reference(_, _info, representation):
    return get_social_data_by_email(representation["email"])

@user.field("social_data")
def resolve_user_social_data(representation, *_):
    return get_social_data_by_email(representation["email"])


mock_social_data = [
    {
        "__typename": "SocialData",
        "email": "jon@test.test",
        "phone": "123-456-7890",
        "avatar_url": "https://avatar.avatar/avatar1.jpg",
        "twitter_url": "https://twitter.twitter/twitter1",
        "facebook_url": "https://facebook.facebook/facebook1"
    },
    {
        "__typename": "SocialData",
        "email": "test@test.test",
        "phone": "555-555-5555",
        "avatar_url": "https://avatar.avatar/avatar2.jpg",
        "twitter_url": "https://twitter.twitter/twitter2",
        "facebook_url": "https://facebook.facebook/facebook2"
    }
]

def get_social_data_by_email(email: str):
    return next((soc for soc in mock_social_data if soc["email"] == email), None)

resolvers = [query, user, social_data]
schema = make_federated_schema(type_defs, resolvers)
app = GraphQL(schema, debug=True)

if (__name__ == "__main__"):
    uvicorn.run("main:app", debug=True, port=4002, reload=True)