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
	// TODO: посчитай сумму и среднее и выведи Sum/Avg
	_ = numbers
	fmt.Println("TODO")
}
