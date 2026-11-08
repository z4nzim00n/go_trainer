package main

import (
	"fmt"
	"strconv"
)

func main() {
	var s string
	fmt.Scan(&s)
	n, err := strconv.Atoi(s)
	// err != nil означает, что строку не удалось разобрать.
	if err != nil {
		fmt.Println("Invalid number")
	} else {
		fmt.Printf("Number: %d\n", n)
	}
}
