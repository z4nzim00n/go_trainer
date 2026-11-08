package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	numbers := make([]int, n)
	for i := range numbers {
		fmt.Scan(&numbers[i])
	}
	// TODO: посчитай min, max и avg
	_ = numbers
	fmt.Println("TODO")
}
