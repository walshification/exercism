var Hamming = function() {};

Hamming.prototype.compute = function(a, b) {
  assert(a.length === b.length, 'DNA strings muse be of equal length.');
  return a.split('').filter(function(char, i) {
    return char != b.charAt(i);
  }).length;
};

module.exports = Hamming;
