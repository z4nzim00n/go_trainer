package main

import (
	"fmt"
	"math"
)

func main() {
	var r float64
	fmt.Scan(&r)
	// Площадь круга: π * r^2. В Go степень через умножение.
	area := math.Pi * r * r
	fmt.Printf("Area: %.2f\n", area)
}
