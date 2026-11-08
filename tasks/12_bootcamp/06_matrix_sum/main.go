package main

import "fmt"

func main() {
	var rows, cols int
	fmt.Scan(&rows, &cols)
	matrix := make([][]int, rows)
	for i := range matrix {
		matrix[i] = make([]int, cols)
		for j := range matrix[i] {
			fmt.Scan(&matrix[i][j])
		}
	}
	// TODO: посчитай сумму элементов
	_ = matrix
	fmt.Println("TODO")
}
