package main

import (
	"fmt"
	"math"
)

func main() {
	var radians float64
	fmt.Scan(&radians)
	degrees := radians * 180 / math.Pi
	fmt.Printf("Degrees: %.2f\n", degrees)
}
