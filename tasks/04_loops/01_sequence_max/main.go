package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	var max int
	fmt.Scan(&max)
	for i := 1; i < n; i++ {
		var x int
		fmt.Scan(&x)
		// TODO: обнови max, если x больше
		_ = x
	}
	fmt.Println(max)
}
