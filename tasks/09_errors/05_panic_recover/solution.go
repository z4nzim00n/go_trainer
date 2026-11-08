package main

import "fmt"

func SafeDivide(a, b int) (result int, err error) {
	defer func() {
		if r := recover(); r != nil {
			err = fmt.Errorf("%v", r)
		}
	}()
	if b == 0 {
		panic("division by zero")
	}
	return a / b, nil
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
