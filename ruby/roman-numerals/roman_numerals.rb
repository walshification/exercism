class Fixnum
  def to_roman
    number = self
    roman_numeral = []
    while number > 0
      if number < 4
        roman_numeral << 'I'
        number -= 1
      elsif number < 5
        roman_numeral << 'IV'
        number -= 4
      elsif number < 9
        roman_numeral << 'V'
        number -= 5
      elsif number < 10
        roman_numeral << 'IX'
        number -= 9
      elsif number < 40
        roman_numeral << 'X'
        number -= 10
      elsif number < 50
        roman_numeral << 'XL'
        number -= 40
      elsif number < 60
        roman_numeral << 'L'
        number -= 50
      elsif number < 90
        roman_numeral << 'LX'
        number -= 60
      elsif number < 100
        roman_numeral << 'XC'
        number -= 90
      elsif number < 400
        roman_numeral << 'C'
        number -= 100
      elsif number < 500
        roman_numeral << 'CD'
        number -= 400
      elsif number < 600
        roman_numeral << 'D'
        number -= 500
      elsif number < 1000
        roman_numeral << 'CM'
        number -= 900
      else
        roman_numeral << 'M'
        number -= 1000
      end
    end
    roman_numeral.join
  end
end

module BookKeeping
  VERSION = 2
end
