class Complement
  def self.of_dna(nucleotide)
    if nucleotide == 'C'
      return 'G'
    elsif nucleotide == 'G'
      return 'C'
    end
  end
end
