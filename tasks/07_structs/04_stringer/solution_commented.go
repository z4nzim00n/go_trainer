package main

import "fmt"

type Temperature float64

// String делает Temperature реализацией fmt.Stringer.
func (t Temperature) String() string {
	return fmt.Sprintf("%.2f°C", float64(t))
}

func main() {
	var t Temperature
	fmt.Scan(&t)
	// %v вызывает метод String.
	fmt.Printf("Temp: %v\n", t)
}
