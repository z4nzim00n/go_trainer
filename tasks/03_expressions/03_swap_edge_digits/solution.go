package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	divisor := 1
	for n/divisor >= 10 {
		divisor *= 10
	}
	first := n / divisor
	last := n % 10
	middle := (n % divisor) / 10
	result := last*divisor + middle*10 + first
	fmt.Println(result)
}
