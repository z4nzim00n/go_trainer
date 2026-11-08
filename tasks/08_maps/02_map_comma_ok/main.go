package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	m := make(map[string]int)
	for i := 0; i < n; i++ {
		var key string
		var value int
		fmt.Scan(&key, &value)
		m[key] = value
	}
	var query string
	fmt.Scan(&query)
	// TODO: используй comma-ok
	fmt.Println("TODO")
}
