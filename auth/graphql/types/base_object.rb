module Types
  class BaseObject < GraphQL::Schema::Object
    include ApolloFederation::Object
  end
end
