package main

import (
	"fmt"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	seen := make(map[int]bool)
	unique := make([]int, 0, n)
	for _, x := range a {
		// Первое появление запоминаем, повторы пропускаем.
		if !seen[x] {
			seen[x] = true
			unique = append(unique, x)
		}
	}
	parts := make([]string, len(unique))
	for i, x := range unique {
		parts[i] = fmt.Sprint(x)
	}
	fmt.Println(strings.Join(parts, " "))
}
