module Types
  class User < BaseObject
    description "User Record"

    key fields: 'id'
    key fields: 'email'

    field :id, ID, null: false
    field :email, String, null: false
    field :username, String, null: false

    def self.resolve_reference(object, _context)
      {
        id: 1,
        username: "Jonjjj",
        email: "jonjjj@test.test"
      }
    end

  end
end
