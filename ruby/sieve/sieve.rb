class Sieve
  attr_reader :composites, :numbers

  def initialize(number)
    @numbers = 1.upto(number)
    @composites = [1]
  end

  def primes
    numbers.select { |i| is_prime?(i) }
  end

  private

  def is_prime?(number)
    return false if composites.include?(number)
    composites.push(*compositize(number))
    true
  end

  def compositize(number)
    1.upto(number) { |i| i * number }
  end
end
