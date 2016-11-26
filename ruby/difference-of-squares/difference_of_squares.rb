class Squares
  attr_reader :number, :natural_numbers

  def initialize(number)
    @number = number
    @natural_numbers = (0..number)
  end

  def difference
    square_of_sum - sum_of_squares
  end

  def square_of_sum
    sum ** 2
  end

  def sum_of_squares
    squares.inject { |sum, i| sum + i }
  end

  private

  def sum
    natural_numbers.inject { |sum, i| sum + i }
  end

  def squares
    natural_numbers.map { |i| i * i }
  end
end

module BookKeeping
  VERSION = 3
end
