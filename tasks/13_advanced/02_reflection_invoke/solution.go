package main

import (
	"fmt"
	"reflect"
)

type Calculator struct{}

func (c Calculator) Add(a, b int) int {
	return a + b
}

func main() {
	var a, b int
	fmt.Scan(&a, &b)

	m := reflect.ValueOf(Calculator{}).MethodByName("Add")
	out := m.Call([]reflect.Value{reflect.ValueOf(a), reflect.ValueOf(b)})
	fmt.Printf("Result: %d\n", out[0].Int())
}
