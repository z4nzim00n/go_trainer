package main

import "fmt"

func main() {
	var name string
	var age int
	// Scan читает string и int по очереди.
	fmt.Scan(&name, &age)
	fmt.Printf("Hello, %s! You are %d.\n", name, age)
}
