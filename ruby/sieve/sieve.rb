class Sieve
  attr_reader :composites, :limit, :numbers

  def initialize(number)
    @limit = number
    @numbers = 1.upto(number)
    @composites = [1]
  end

  def primes
    numbers.select { |i| is_prime?(i) }
  end

  private

  def is_prime?(i)
    return false if composites.include?(i)
    composites.push(*compositize(i))
    true
  end

  def compositize(prime)
    1.upto(limit).map { |i| i * prime }
  end
end
