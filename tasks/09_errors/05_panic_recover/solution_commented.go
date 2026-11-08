package main

import "fmt"

// SafeDivide перехватывает собственную панику и превращает её в ошибку.
func SafeDivide(a, b int) (result int, err error) {
	defer func() {
		// recover() возвращает значение panic или nil.
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
