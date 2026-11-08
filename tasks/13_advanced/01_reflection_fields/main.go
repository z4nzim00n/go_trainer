package main

import "fmt"

type Person struct {
	Name string
	Age  int
}

func main() {
	var p Person
	fmt.Scan(&p.Name, &p.Age)
	// TODO: выведи поля через reflection
	_ = p
	fmt.Println("TODO")
}
