class Sieve
  attr_reader :numbers

  def initialize(number)
    @numbers = (1..number)
  end

  def primes
    numbers.select { |i| is_prime?(i) }
  end

  private

  def is_prime?(number)
    return false if number < 2
  end
end
