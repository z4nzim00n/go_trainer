package main

import "fmt"

func main() {
	var a, b int
	// Scan принимает указатели, поэтому нужен &.
	fmt.Scan(&a, &b)
	fmt.Println(b, a)
}
