package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	divisor := 1
	for n/divisor >= 10 {
		divisor *= 10
	}
	// TODO: поменяй первую и последнюю цифры и выведи результат
	_ = divisor
	fmt.Println("TODO")
}
