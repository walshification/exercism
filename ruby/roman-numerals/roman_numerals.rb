NUMERALS = [
  { '4' => ['I', 1] },
  { '5' => ['IV', 4] },
  { '9' => ['V', 5] },
  { '10' => ['IX', 9] },
  { '40' => ['X', 10] },
  { '50' => ['XL', 40] },
  { '60' => ['L', 50] },
  { '90' => ['LX', 60] },
  { '100' => ['XC', 90] },
  { '400' => ['C', 100] },
  { '500' => ['CD', 400] },
  { '900' => ['D', 500] },
  { '1000' => ['CM', 900] },
  { '999999999' => ['M', 1000] },
]

class Fixnum
  def to_roman
    number = self
    roman_numeral = []
    while number > 0
      NUMERALS.each do |limit_pair|
        if number < limit_pair.keys.first.to_i
          roman_numeral << limit_pair[limit_pair.keys.first][0]
          number -= limit_pair[limit_pair.keys.first][1]
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
