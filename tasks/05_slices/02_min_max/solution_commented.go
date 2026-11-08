package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	numbers := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&numbers[i])
	}
	// Первый элемент — корректный старт для обоих экстремумов.
	min, max := numbers[0], numbers[0]
	for _, x := range numbers[1:] {
		if x < min {
			min = x
		}
		if x > max {
			max = x
		}
	}
	fmt.Printf("Min: %d\n", min)
	fmt.Printf("Max: %d\n", max)
}
