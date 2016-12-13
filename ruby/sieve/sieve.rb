class Sieve
  def initialize(number)
    @limit = number
  end

  def primes
    @primes ||= generate_primes
  end

  private

  def generate_primes
    integers.each do |prime|
      next unless prime
      mark_composites(prime)
      break if prime * prime >= @limit
    end
    @primes.compact
  end

  def integers
    @primes = 0.upto(@limit).to_a
    @primes[0], @primes[1] = nil  # skip 0 and 1
    @primes
  end

  def mark_composites(prime)
    ((prime * prime)..@limit).step(prime) do |composite|
      @primes[composite] = nil
    end
  end
end

module BookKeeping
  VERSION = 1
end
