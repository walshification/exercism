FACTOR_CHECKS = [ 'pling', 'plang', 'plong' ]

class Raindrops
  def self.convert(number)
    raindrops = FACTOR_CHECKS.map do |check|
      Raindrops.send(check, number)
    end

    # check raindrops for values other than nil.
    if raindrops.select { |drop| drop }.empty?
      number.to_s
    else
      raindrops.join
    end
  end

  def self.pling(number)
    'Pling' if number % 3 == 0
  end

  def self.plang(number)
    'Plang' if number % 5 == 0
  end

  def self.plong(number)
    'Plong' if number % 7 == 0
  end
end

module BookKeeping
  VERSION = 3
end
