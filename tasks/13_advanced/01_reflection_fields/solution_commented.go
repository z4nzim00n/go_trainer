package main

import (
	"fmt"
	"reflect"
	"strings"
)

type Person struct {
	Name string
	Age  int
}

func main() {
	var p Person
	fmt.Scan(&p.Name, &p.Age)

	v := reflect.ValueOf(p) // значение
	t := v.Type()           // описание типа
	parts := make([]string, 0, t.NumField())
	for i := 0; i < t.NumField(); i++ {
		// t.Field(i) — имя и тип поля, v.Field(i) — его значение.
		parts = append(parts, t.Field(i).Name+"="+fmt.Sprint(v.Field(i).Interface()))
	}
	fmt.Println(strings.Join(parts, " "))
}
