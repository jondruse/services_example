class MutationType < GraphQL::Schema::Object

  field :signup, mutation: Mutations::Signup

end
