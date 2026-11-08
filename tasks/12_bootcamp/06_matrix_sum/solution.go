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
	sum := 0
	for _, row := range matrix {
		for _, x := range row {
			sum += x
		}
	}
	fmt.Printf("Sum: %d\n", sum)
}
