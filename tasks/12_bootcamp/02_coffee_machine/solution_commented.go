package main

import "fmt"

const price = 50

func main() {
	var n int
	fmt.Scan(&n)
	total := 0
	for i := 0; i < n; i++ {
		var coin int
		fmt.Scan(&coin)
		total += coin
	}
	// Граница total == price тоже считается успехом.
	if total >= price {
		fmt.Printf("Coffee: %d\n", total-price)
	} else {
		fmt.Printf("Need: %d\n", price-total)
	}
}
