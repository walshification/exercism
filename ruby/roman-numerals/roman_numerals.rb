class Fixnum
  def to_roman
    if self == 1
      'I'
    elsif self == 2
      'II'
    end
  end
end
