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

	// Стадия 1: генератор.
	go func() {
		for _, x := range values {
			in <- x
		}
		close(in)
	}()

	// Стадия 2: квадраты. Закрывает out, когда in опустеет.
	go func() {
		for x := range in {
			out <- x * x
		}
		close(out)
	}()

	// Главная горутина читает результаты.
	sum := 0
	for x := range out {
		sum += x
	}
	fmt.Printf("Sum: %d\n", sum)
}
