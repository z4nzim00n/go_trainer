package main

import "fmt"

func isPrime(n int) bool {
	// 0, 1 и отрицательные числа не простые.
	if n < 2 {
		return false
	}
	// Достаточно проверить делители до sqrt(n).
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	var n int
	fmt.Scan(&n)
	if isPrime(n) {
		fmt.Println("Prime")
	} else {
		fmt.Println("Not prime")
	}
}
