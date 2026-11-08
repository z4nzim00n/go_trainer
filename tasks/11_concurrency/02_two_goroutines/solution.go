package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	ch := make(chan int, 2)
	go func() { ch <- a * 2 }()
	go func() { ch <- b * 2 }()
	sum := <-ch + <-ch
	fmt.Printf("Sum: %d\n", sum)
}
