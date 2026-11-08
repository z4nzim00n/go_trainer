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
	// Два указателя идут навстречу друг другу.
	for i, j := 0, len(a)-1; i < j; i, j = i+1, j-1 {
		a[i], a[j] = a[j], a[i]
	}
	parts := make([]string, len(a))
	for i, x := range a {
		parts[i] = fmt.Sprint(x)
	}
	fmt.Println(strings.Join(parts, " "))
}
