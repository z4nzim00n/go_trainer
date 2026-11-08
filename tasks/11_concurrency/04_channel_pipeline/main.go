package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	values := make([]int, n)
	for i := range values {
		fmt.Scan(&values[i])
	}
	// TODO: собери конвейер и посчитай сумму квадратов
	_ = values
	fmt.Println("TODO")
}
