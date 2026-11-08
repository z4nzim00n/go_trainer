package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	values := make([]int, n)
	for i := range values {
		fmt.Scan(&values[i])
	}

	in := make(chan int)
	out := make(chan int)

	go func() {
		for _, x := range values {
			in <- x
		}
		close(in)
	}()

	go func() {
		for x := range in {
			out <- x * x
		}
		close(out)
	}()

	sum := 0
	for x := range out {
		sum += x
	}
	fmt.Printf("Sum: %d\n", sum)
}
