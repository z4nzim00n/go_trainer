package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)

	// Буфер на 2 значения: обе горутины смогут отправить результат.
	ch := make(chan int, 2)
	go func() { ch <- a * 2 }()
	go func() { ch <- b * 2 }()

	// Читаем два значения; порядок не важен для суммы.
	sum := <-ch + <-ch
	fmt.Printf("Sum: %d\n", sum)
}
