class Raindrops
  def self.convert(number)
    if number % 3 == 0
      'Pling'
    elsif number % 5 == 0
      'Plang'
    elsif number % 7 == 0
      'Plong'
    elsif number % 6 == 0
      'Pling'
    else
      number.to_s
    end
  end
end

module BookKeeping
  VERSION = 3
end
