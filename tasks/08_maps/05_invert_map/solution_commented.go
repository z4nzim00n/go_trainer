package main

import (
	"fmt"
	"sort"
)

func main() {
	var n int
	fmt.Scan(&n)
	direct := make(map[string]int)
	for i := 0; i < n; i++ {
		var word string
		var num int
		fmt.Scan(&word, &num)
		direct[word] = num
	}

	// Меняем ключи и значения местами.
	inverse := make(map[int]string)
	for word, num := range direct {
		inverse[num] = word
	}

	nums := make([]int, 0, len(inverse))
	for num := range inverse {
		nums = append(nums, num)
	}
	sort.Ints(nums)

	for _, num := range nums {
		fmt.Printf("%d: %s\n", num, inverse[num])
	}
}
