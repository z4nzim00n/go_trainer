package main

import "fmt"

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	shift := k % n
	// TODO: выведи элементы в порядке сдвига влево
	_ = shift
	fmt.Println("TODO")
}
