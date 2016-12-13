NUMERALS_TO_LIMITS = [
  ['M', 1000],
  ['CM', 900],
  ['D', 500],
  ['CD', 400],
  ['C', 100],
  ['XC', 90],
  ['L', 50],
  ['XL', 40],
  ['X', 10],
  ['IX', 9],
  ['V', 5],
  ['IV', 4],
  ['I', 1],
]

class Fixnum
  def to_roman
    number = self
    roman_numeral = []
    while number > 0
      NUMERALS_TO_LIMITS.each do |numeral, limit|
        if number >= limit
          roman_numeral << numeral
          number -= limit
          break
        end
      end
    end
    roman_numeral.join
  end
end

module BookKeeping
  VERSION = 2
end
