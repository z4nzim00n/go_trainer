package main

import "fmt"

type Person struct {
	Name string
}

type Employee struct {
	Person
	Company string
}

func main() {
	var e Employee
	fmt.Scan(&e.Name, &e.Company)
	fmt.Printf("Name: %s, Company: %s\n", e.Name, e.Company)
}
