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
		if x > max {
			max = x
		}
	}
	fmt.Println(max)
}
