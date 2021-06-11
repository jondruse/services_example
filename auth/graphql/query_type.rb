class QueryType < GraphQL::Schema::Object
  description "The query root of this schema"

  field :current_user, Types::User, null: false

  def current_user
    {
      id: 1,
      username: "Jon"
    }
  end

end
