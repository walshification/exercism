class Sieve
  def initialize(limit)
    @limit = limit
    @square_root_of_limit = Math.sqrt(limit).ceil
  end

  def primes
    @primes ||= generate_primes
  end

  private

  def generate_primes
    integers.map do |prime|
      next if prime.nil?
      mark_composites(prime)
    end
    integers.compact
  end

  def integers
    @integers ||= Array(2..@limit)
  end

  def mark_composites(prime)
    ((prime * prime)..@limit).step(prime) do |composite|
      integers[composite - 2] = nil
    end
  end
end

module BookKeeping
  VERSION = 1
end
