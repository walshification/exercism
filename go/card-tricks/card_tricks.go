package cards

// FavoriteCards returns a slice with the cards 2, 6 and 9 in that order.
func FavoriteCards() []int {
	return []int{2, 6, 9}
}

// GetItem retrieves an item from a slice at given position.
// If the index is out of range, we want it to return -1.
func GetItem(slice []int, index int) int {
	if checkOutOfBounds(index, len(slice)) {
		return -1
	}
	return slice[index]
}

// SetItem writes an item to a slice at given position overwriting an existing value.
// If the index is out of range the value needs to be appended.
func SetItem(slice []int, index, value int) []int {
	if checkOutOfBounds(index, len(slice)) {
		return append(slice, value)
	}
	slice[index] = value
	return slice
}

// PrependItems adds an arbitrary number of values at the front of a slice.
func PrependItems(slice []int, values ...int) []int {
	return append(values, slice...)
}

// RemoveItem removes an item from a slice by modifying the existing slice.
func RemoveItem(slice []int, index int) []int {
	sliceLength := len(slice)
	if checkOutOfBounds(index, sliceLength) {
		return slice
	}
	removedSlice := slice[:index]
	// If the removed index is not at the end ...
	if index+1 < sliceLength {
		// tack on the rest of the slice after the removed index.
		removedSlice = append(removedSlice, slice[index+1:]...)
	}
	return removedSlice
}

// checkOutOfBounds returns true if an index is not found in a given slice.
func checkOutOfBounds(index, sliceLength int) bool {
	return index < 0 || index >= sliceLength
}
