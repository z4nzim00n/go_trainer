package main

import (
	"fmt"
	"math"
)

func main() {
	var r float64
	fmt.Scan(&r)
	area := math.Pi * r * r
	fmt.Printf("Area: %.2f\n", area)
}
