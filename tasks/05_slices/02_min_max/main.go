package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	numbers := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&numbers[i])
	}
	// TODO: найди минимум и максимум и выведи Min/Max
	_ = numbers
	fmt.Println("TODO")
}
