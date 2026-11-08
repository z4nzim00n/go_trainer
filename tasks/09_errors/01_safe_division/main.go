package main

import (
	"errors"
	"fmt"
)

// TODO: реализуй Divide
func Divide(a, b int) (int, error) {
	return 0, errors.New("not implemented")
}

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	result, err := Divide(a, b)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Printf("Result: %d\n", result)
	}
}
