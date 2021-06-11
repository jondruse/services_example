module Mutations
  class Signup < GraphQL::Schema::Mutation

    argument :username, String, required: true


    field :user, Types::User, null: true

    def resolve(username:)
      {
        user: {
          id: 1,
          username: username
        }
      }
    end

  end
end

