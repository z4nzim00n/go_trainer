package main

import "fmt"

type User struct {
	Name string
	Age  int
}

func NewUser(name string, age int) *User {
	return &User{Name: name, Age: age}
}

func main() {
	var name string
	var age int
	fmt.Scan(&name, &age)
	u := NewUser(name, age)
	fmt.Printf("Name: %s, Age: %d\n", u.Name, u.Age)
}
