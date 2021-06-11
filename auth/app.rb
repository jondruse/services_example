require 'bundler'
Bundler.require

loader = Zeitwerk::Loader.new
loader.push_dir('graphql')
loader.setup


class App < Sinatra::Base
  use Rack::JSONBodyParser

  post '/v1' do
    result = AuthServiceSchema.execute(
      params[:query],
      variables: params[:variables],
      context: { current_user: nil },
    )
    json result
  end
end
