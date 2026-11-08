package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	result := 0
	for i := 0; i < n; i++ {
		var x int
		fmt.Scan(&x)
		result ^= x
	}
	fmt.Println(result)
}
