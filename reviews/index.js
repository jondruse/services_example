const { ApolloServer, gql } = require('apollo-server');
const { buildFederatedSchema } = require('@apollo/federation');

const typeDefs = gql`
  type Query {
    reviews: [Review!]
  }

  type Mutation {
    createReview(userId: ID!, rating: Int!): CreateReviewPayload
  }

  type CreateReviewPayload {
    review: Review!
  }

  type Review @key(fields: "id") {
    id: ID!
    rating: Int!
    user: User!
  }

  extend type User @key(fields: "id") {
    id: ID! @external
    reviews: [Review!]
  }
`;

const resolvers = {
  Mutation: {
    createReview(parent, args, context, info) {
      return { review: { id: "1", rating: args.rating, userId: args.userId } }
    }
  },
  Query: {
    reviews() {
      return [{ id: "1", rating: 2, userId: 1 }]
    }
  },
  User: {
    reviews(object) {
      return [{ id: "1", rating: 2, userId: object.id }]
    }
  },
  Review: {
    __resolveReference(user){
      return { id: 1, rating: 2, userId: user.id }
    },
    user(object){
      return { __typename: "User", id: object.userId }
    }
  }
}

const server = new ApolloServer({
  schema: buildFederatedSchema([{ typeDefs, resolvers }]),
  context: params => () => {
    console.log(params.req.body.query);
  }
});

server.listen(4001).then(({ url }) => {
    console.log(`🚀 Server ready at ${url}`);
});

