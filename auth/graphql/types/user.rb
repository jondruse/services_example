module Types
  class User < BaseObject
    description "User Record"

    key fields: 'id'

    field :id, ID, null: false
    field :username, String, null: false

    def self.resolve_reference(object, _context)
      {
        id: 1,
        username: "Jonjjj"
      }
    end

  end
end
