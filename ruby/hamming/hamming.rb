class Hamming

  def self.compute(strand1, strand2)
    (0..strand1.length).select { |i| strand1[i] != strand2[i] }.count
  end

end
