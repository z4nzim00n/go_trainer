package main

import "fmt"

const price = 50

func main() {
	var n int
	fmt.Scan(&n)
	total := 0
	for i := 0; i < n; i++ {
		var coin int
		fmt.Scan(&coin)
		total += coin
	}
	// TODO: реши, хватает ли денег
	_ = total
	fmt.Println("TODO")
}
