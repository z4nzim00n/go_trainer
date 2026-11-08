package main

import "fmt"

func main() {
	var name string
	var age int
	fmt.Scan(&name, &age)
	fmt.Printf("Hello, %s! You are %d.\n", name, age)
}
