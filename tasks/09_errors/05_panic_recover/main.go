package main

import "fmt"

// TODO: реализуй SafeDivide с panic и recover
func SafeDivide(a, b int) (int, error) {
	return 0, nil
}

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	result, err := SafeDivide(a, b)
	if err != nil {
		fmt.Println("Recovered:", err)
	} else {
		fmt.Printf("Result: %d\n", result)
	}
}
