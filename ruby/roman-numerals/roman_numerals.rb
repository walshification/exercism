class Fixnum
  def to_roman
    case self
    when 1
      return 'I'
    when 2
      return 'II'
    when 3
      return 'III'
    when 4
      return 'IV'
    when 5
      return 'V'
    when 6
      return 'VI'
    when 9
      return 'IX'
    end
  end
end
