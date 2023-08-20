package blackjack

// ParseCard returns the integer value of a card following blackjack ruleset.
func ParseCard(card string) int {
	var value int
	switch card {
	case "ace":
		value = 11
	case "two":
		value = 2
	case "three":
		value = 3
	case "four":
		value = 4
	case "five":
		value = 5
	case "six":
		value = 6
	case "seven":
		value = 7
	case "eight":
		value = 8
	case "nine":
		value = 9
	case "ten":
		value = 10
	case "jack":
		value = 10
	case "queen":
		value = 10
	case "king":
		value = 10
	default:
		value = 0
	}
	return value
}

// FirstTurn returns the decision for the first turn, given two cards of the
// player and one card of the dealer.
func FirstTurn(card1, card2, dealerCard string) string {
	card1Value := ParseCard(card1)
	card2Value := ParseCard(card2)
	playerValue := card1Value + card2Value
	dealerValue := ParseCard(dealerCard)
	var decision string
	switch {
	case card1 == "ace" && card2 == "ace":
		// If you have a pair of aces you must always split them.
		decision = "P"
	case playerValue == 21 && dealerValue < 10:
		// If you have a Blackjack (two cards that sum up to a value of 21), and the dealer
		// does not have an ace, a figure or a ten then you automatically win.
		decision = "W"
	case playerValue == 21 && dealerValue >= 10:
		// If the dealer does have any of those cards then you'll have to stand and wait
		// for the reveal of the other card.
		decision = "S"
	case playerValue >= 17 && playerValue < 21:
		// If your cards sum up to a value within the range [17, 20] you should always stand.
		decision = "S"
	case playerValue >= 12 && playerValue < 17 && dealerValue < 7:
		// If your cards sum up to a value within the range [12, 16] you should always stand
		decision = "S"
	case playerValue >= 12 && playerValue < 17 && dealerValue >= 7:
		// unless the dealer has a 7 or higher, in which case you should always hit.
		decision = "H"
	case playerValue <= 11:
		// If your cards sum up to 11 or lower you should always hit.
		decision = "H"
	}
	return decision
}
