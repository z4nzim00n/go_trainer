package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	seen := make(map[int]bool)
	unique := make([]int, 0)
	for i := 0; i < n; i++ {
		var x int
		fmt.Scan(&x)
		if !seen[x] {
			seen[x] = true
			unique = append(unique, x)
		}
	}
	sort.Ints(unique)
	parts := make([]string, len(unique))
	for i, x := range unique {
		parts[i] = fmt.Sprint(x)
	}
	fmt.Printf("Unique: %d\n", len(unique))
	fmt.Println(strings.Join(parts, " "))
}
