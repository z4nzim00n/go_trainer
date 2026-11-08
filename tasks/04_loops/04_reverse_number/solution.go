package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	if n < 0 {
		n = -n
	}
	reversed := 0
	for n > 0 {
		reversed = reversed*10 + n%10
		n /= 10
	}
	fmt.Println(reversed)
}
