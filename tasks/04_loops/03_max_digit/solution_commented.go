package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	if n < 0 {
		n = -n
	}
	// Цифры лежат в диапазоне 0..9, поэтому 0 — корректный старт.
	max := 0
	for n > 0 {
		digit := n % 10
		if digit > max {
			max = digit
		}
		n /= 10
	}
	fmt.Println(max)
}
