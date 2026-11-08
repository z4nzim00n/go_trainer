package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// Делится на 3 ИЛИ оканчивается на 7.
	result := n%3 == 0 || n%10 == 7
	fmt.Println(result)
}
