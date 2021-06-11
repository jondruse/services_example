class AuthServiceSchema < GraphQL::Schema
  include ApolloFederation::Schema

  query QueryType
  mutation MutationType
end
