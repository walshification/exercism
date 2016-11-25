class Complement
  def self.of_dna(nucleotides)
    transcribed = nucleotides.chars.map do |nucleotide|
      DnaTranscriber.transcribe(nucleotide)
    end
    transcribed.join
  end
end


class DnaTranscriber
  def self.transcribe(nucleotide)
    case nucleotide
    when 'C'
      return 'G'
    when 'G'
      return 'C'
    when 'T'
      return 'A'
    when 'A'
      return 'U'
    end
  end
end
