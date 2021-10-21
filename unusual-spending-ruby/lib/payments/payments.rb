class Payment
  def initialize
    @category =  ['fun', 'food', 'groceries', 'other'].sample
    @amount = rand(5.2...76.9)
  end
end

def get_payments(user_id, month)
  Array.new(rand(1..100)) { Payment.new }
end
