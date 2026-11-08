package main

import "fmt"

func isPrime(n int) bool {
	// TODO: реализуй проверку
	return false
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
