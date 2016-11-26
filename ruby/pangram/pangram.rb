class Pangram
  def self.pangram?(phrase)
    return if phrase.empty?
    alphabet = ('a'..'z')
    phrase = phrase.downcase

    alphabet.each do |letter|
      next if phrase.include?(letter)
      return false
    end
    true
  end
end

module BookKeeping
  VERSION = 3
end
