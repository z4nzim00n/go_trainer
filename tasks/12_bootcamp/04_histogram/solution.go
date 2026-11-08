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
	for v := 1; v <= maxValue; v++ {
		if counts[v] == 0 {
			continue
		}
		fmt.Printf("%d: %s\n", v, strings.Repeat("*", counts[v]))
	}
}
