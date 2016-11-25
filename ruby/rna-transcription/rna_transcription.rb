class Complement
  def self.of_dna(nucleotide)
    case nucleotide
    when 'C'
      return 'G'
    when 'G'
      return 'C'
    when 'T'
      return 'A'
    end
  end
end
