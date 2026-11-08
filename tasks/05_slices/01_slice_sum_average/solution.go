package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	numbers := make([]int, 0, n)
	for i := 0; i < n; i++ {
		var x int
		fmt.Scan(&x)
		numbers = append(numbers, x)
	}
	sum := 0
	for _, x := range numbers {
		sum += x
	}
	avg := 0.0
	if n > 0 {
		avg = float64(sum) / float64(n)
	}
	fmt.Printf("Sum: %d\n", sum)
	fmt.Printf("Avg: %.2f\n", avg)
}
