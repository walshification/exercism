class Squares
  attr_reader :number

  def initialize(number)
    @number = number
  end

  def square_of_sum
    total = (0..number).inject { |sum, i| sum + i }
    total * total
  end
end
