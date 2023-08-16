// Package weather provides tools to describe the current weather conditions for a location.
package weather

// CurrentCondition represents the weather condition at the moment.
var CurrentCondition string

// CurrentLocation represents the geographic place under weather watch.
var CurrentLocation string

// Forecast takes a city string and condition string and returns a string value describing
// the weather conditions at the city.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
