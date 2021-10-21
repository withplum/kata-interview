Dir.glob(File.expand_path('lib/**/*.rb')) { |file| require file }

RSpec.configure do |config|
  config.color = true
end
