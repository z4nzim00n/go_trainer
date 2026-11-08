package main

import "fmt"

type Calculator struct{}

func (c Calculator) Add(a, b int) int {
	return a + b
}

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	// TODO: вызови Add через reflection
	_ = a
	_ = b
	fmt.Println("TODO")
}
