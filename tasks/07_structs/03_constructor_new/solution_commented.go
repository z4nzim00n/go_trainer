package main

import "fmt"

type User struct {
	Name string
	Age  int
}

// NewUser — конструктор: создаёт User и возвращает указатель на него.
func NewUser(name string, age int) *User {
	return &User{Name: name, Age: age}
}

func main() {
	var name string
	var age int
	fmt.Scan(&name, &age)
	u := NewUser(name, age)
	// С указателем поля читаются так же: u.Name.
	fmt.Printf("Name: %s, Age: %d\n", u.Name, u.Age)
}
