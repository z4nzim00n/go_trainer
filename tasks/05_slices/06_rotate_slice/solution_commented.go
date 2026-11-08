package main

import "fmt"

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	// Сдвиг на N возвращает срез в исходное состояние.
	shift := k % n
	for i := 0; i < n; i++ {
		if i > 0 {
			fmt.Print(" ")
		}
		// Остаток заворачивает индекс в 0..n-1.
		fmt.Print(a[(i+shift)%n])
	}
	fmt.Println()
}
