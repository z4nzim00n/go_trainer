package main

import (
	"fmt"
	"strings"
)

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	a := make([]int, n)
	for i := range a {
		fmt.Scan(&a[i])
	}
	if n == 0 {
		fmt.Println()
		return
	}
	k = k % n
	result := append([]int{}, a[n-k:]...)
	result = append(result, a[:n-k]...)
	parts := make([]string, len(result))
	for i, x := range result {
		parts[i] = fmt.Sprint(x)
	}
	fmt.Println(strings.Join(parts, " "))
}
