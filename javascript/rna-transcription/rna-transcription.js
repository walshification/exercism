var DnaTranscriber = function() {};

DnaTranscriber.prototype.toRna = function(string) {
  var dnaMap = { C: 'G', G: 'C', A: 'U', T: 'A' };
  if(!string.split('').every(function(nucleotide) {
    return Object.keys(dnaMap).includes(nucleotide);
  })) { throw new Error('Invalid input'); }

  return string.split('').reduce(function(transcribed, nucleotide) {
    return transcribed += dnaMap[nucleotide];
  }, '');
};

module.exports = DnaTranscriber;
