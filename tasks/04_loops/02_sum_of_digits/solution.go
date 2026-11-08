package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	if n < 0 {
		n = -n
	}
	sum := 0
	for n > 0 {
		sum += n % 10
		n /= 10
	}
	fmt.Println(sum)
}
