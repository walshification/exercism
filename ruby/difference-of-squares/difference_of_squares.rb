class Squares
  attr_reader :number

  def initialize(number)
    @number = number
  end

  def square_of_sum
    total = (0..number).inject { |sum, i| sum + i }
    total * total
  end

  def sum_of_squares
    squares.inject { |sum, i| sum + i }
  end

  def squares
    (0..number).map { |i| i * i }
  end
end
