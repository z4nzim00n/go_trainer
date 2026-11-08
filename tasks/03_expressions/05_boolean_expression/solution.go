package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	result := n%3 == 0 || n%10 == 7
	fmt.Println(result)
}
