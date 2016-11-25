class Raindrops
  def self.convert(number)
    raindrops = []
    if number % 3 == 0
      raindrops << 'Pling'
    end
    if number % 5 == 0
      raindrops << 'Plang'
    end
    if number % 7 == 0
      raindrops << 'Plong'
    end
    if raindrops.empty?
      number.to_s
    else
      raindrops.join
    end
  end
end

module BookKeeping
  VERSION = 3
end
