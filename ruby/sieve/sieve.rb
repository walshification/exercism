class Number
  attr_reader :value, :marked

  def initialize(value)
    @marked = false
    @value = value
  end

  def mark
    @marked = true
  end
end

class Sieve
  def initialize(number)
    @limit = number
    @primes = 2.upto(number).map { |prime| Number.new(prime) }
  end

  def primes
    @primes.each do |prime|
      next if prime.marked
      mark_composites(prime)
    end
    @primes.reject { |prime| prime.marked }.map { |prime| prime.value }
  end

  private

  def mark_composites(prime)
    @primes.each do |integer|
      next if integer.value == prime.value || integer.marked
      integer.mark if integer.value % prime.value == 0
    end
  end
end

module BookKeeping
  VERSION = 1
end
