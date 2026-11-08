package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	if n == 0 {
		fmt.Println("Min: 0")
		fmt.Println("Max: 0")
		fmt.Println("Avg: 0.00")
		return
	}

	numbers := make([]int, n)
	for i := range numbers {
		fmt.Scan(&numbers[i])
	}

	// Начинаем с первого элемента, а не с нуля.
	min, max, sum := numbers[0], numbers[0], 0
	for _, x := range numbers {
		if x < min {
			min = x
		}
		if x > max {
			max = x
		}
		sum += x
	}
	fmt.Printf("Min: %d\n", min)
	fmt.Printf("Max: %d\n", max)
	fmt.Printf("Avg: %.2f\n", float64(sum)/float64(n))
}
