package main

import "fmt"

// Max работает для int и float64: тип T выводится из аргументов.
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
