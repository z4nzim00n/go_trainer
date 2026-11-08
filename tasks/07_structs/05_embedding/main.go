package main

import "fmt"

type Person struct {
	Name string
}

// TODO: опиши Employee со встроенным Person и полем Company

type Employee struct {
	Person
	Company string
}

func main() {
	var e Employee
	fmt.Scan(&e.Name, &e.Company)
	// TODO: выведи имя и компанию
	fmt.Println("TODO")
}
