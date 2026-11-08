package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	// Приводим сумму к float64 ДО деления, иначе дробь потеряется.
	average := float64(a+b) / 2.0
	fmt.Printf("Avg: %.2f\n", average)
}
