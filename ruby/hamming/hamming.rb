class Hamming

  def self.compute(strand1, strand2)
    strand1_nucs = strand1.chars
    strand2_nucs = strand2.chars
    hamming = strand1_nucs.select.with_index do |nucleotide, i|
      nucleotide unless nucleotide == strand2_nucs[i]
    end
    hamming.count
  end

end
