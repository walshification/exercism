STUMPS = ['1', '2', '3']

EDGES = ['4', '9']

class Fixnum
  def to_roman
    case self
    when 1, 2, 3
      return translate(self.to_s.split)
    when 4
      return translate(self.to_s.split)
    when 5
      return 'V'
    when 6
      return 'VI'
    when 9
      return 'IX'
    end
  end

  def translate(digits)
    roman_numeral = []
    if EDGES.include?(digits.last)
      roman_numeral << 'I'
      roman_numeral << if digits.last == '4' then 'V' else 'X' end
    end
    if digits.last < 4
      digits.last.to_i.times do
        roman_numeral << 'I'
      end
    elsif digits.last < 9

    end
    roman_numeral.join
  end
end
