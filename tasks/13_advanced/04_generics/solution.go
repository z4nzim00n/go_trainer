package main

import "fmt"

func Max[T int | float64](a, b T) T {
	if a > b {
		return a
	}
	return b
}

func main() {
	var a, b float64
	fmt.Scan(&a, &b)
	fmt.Printf("Max: %.2f\n", Max(a, b))
}
