package main

import (
	"fmt"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	counts := make(map[int]int)
	maxValue := 0
	for i := 0; i < n; i++ {
		var x int
		fmt.Scan(&x)
		counts[x]++
		if x > maxValue {
			maxValue = x
		}
	}
	// TODO: выведи гистограмму по возрастанию
	_ = strings.Repeat
	_ = maxValue
	fmt.Println("TODO")
}
