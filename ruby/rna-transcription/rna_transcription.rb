DNA_MAP = { 'C' => 'G', 'G' => 'C', 'T' => 'A', 'A' => 'U' }

class Complement
  def self.of_dna(nucleotides)
    transcribed = nucleotides.chars.map do |nucleotide|
      return '' unless DNA_MAP.keys.include?(nucleotide)
      DNA_MAP[nucleotide]
    end
    transcribed.join
  end
end

module BookKeeping
  VERSION = 4
end
