package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	// TODO: разверни a и выведи элементы через пробел
	_ = a
	fmt.Println("TODO")
}
