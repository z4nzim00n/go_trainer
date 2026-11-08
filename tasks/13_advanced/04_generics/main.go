package main

import "fmt"

// TODO: сделай Max обобщённой
func Max[T int | float64](a, b T) T {
	return a
}

func main() {
	var a, b float64
	fmt.Scan(&a, &b)
	// TODO: выведи максимум
	_ = a
	_ = b
	fmt.Println("TODO")
}
