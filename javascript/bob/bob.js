//
// This is only a SKELETON file for the "Bob" exercise. It's been provided as a
// convenience to get you started writing code faster.
//

var Bob = function() {};

Bob.prototype.hey = function(input) {
  var output = '';
  switch(true) {
    case input.replace(/\s/g, '') === '':
      output += 'Fine. Be that way!';
      break;
    case isACalmQuestion(input):
      output += 'Sure.';
      break;
    case containsOnlyNumbers(input):
      output += 'Whatever.';
      break;
    case isShouting(input):
      output += 'Whoa, chill out!';
      break;
    default:
      output += 'Whatever.';
  }
  return output;
};

function isShouting(input) {
  return input === input.toUpperCase();
}

function isACalmQuestion(input) {
  return input.substr(-1) === '?' && isNotShouting(input);
}

function isNotShouting(input) {
  return !isShouting(input) || containsOnlyNumbers(input)
}

function containsOnlyNumbers(input) {
  return /^[\d,\s]+$/.test(input.slice(0, input.length - 1));
}

module.exports = Bob;
