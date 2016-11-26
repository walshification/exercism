class Sieve
  attr_reader :composites, :limit

  def initialize(number)
    @limit = number
    @primes = 2.upto(number)
    @composites = [1]
  end

  def primes
    @primes.select { |digit| is_prime?(digit) }
  end

  private

  def is_prime?(digit)
    return false if composites.include?(digit)
    composites.push(*compositize(digit))
    true
  end

  def compositize(prime)
    1.upto(limit).map { |i| i * prime }
  end
end

module BookKeeping
  VERSION = 1
end
