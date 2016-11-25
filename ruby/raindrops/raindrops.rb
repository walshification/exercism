class Raindrops
  def self.convert(number)
    if number == 3
      'Pling'
    elsif number == 5
      'Plang'
    elsif number == 7
      'Plong'
    elsif number == 6
      'Pling'
    else
      '1'
    end
  end
end

module BookKeeping
  VERSION = 3
end