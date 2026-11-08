package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	// TODO: убери повторы, сохранив порядок, и выведи через пробел
	_ = a
	fmt.Println("TODO")
}
