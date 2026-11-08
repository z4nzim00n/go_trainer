package main

import (
	"fmt"
	"strconv"
)

func main() {
	var s string
	fmt.Scan(&s)
	n, err := strconv.Atoi(s)
	if err != nil {
		fmt.Println("Invalid number")
	} else {
		fmt.Printf("Number: %d\n", n)
	}
}
