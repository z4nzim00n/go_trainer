package main

import "fmt"

type User struct {
	Name string
	Age  int
}

// TODO: напиши NewUser
func NewUser(name string, age int) *User {
	return &User{}
}

func main() {
	var name string
	var age int
	fmt.Scan(&name, &age)
	u := NewUser(name, age)
	// TODO: выведи Name и Age
	_ = u
	fmt.Println("TODO")
}
