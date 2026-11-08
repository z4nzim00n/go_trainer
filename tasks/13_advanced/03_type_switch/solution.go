package main

import (
	"fmt"
	"strconv"
)

func main() {
	var s string
	fmt.Scan(&s)

	var v interface{}
	if n, err := strconv.Atoi(s); err == nil {
		v = n
	} else if f, err := strconv.ParseFloat(s, 64); err == nil {
		v = f
	} else {
		v = s
	}

	switch x := v.(type) {
	case int:
		fmt.Printf("int: %d\n", x)
	case float64:
		fmt.Printf("float: %.2f\n", x)
	case string:
		fmt.Printf("string: %s\n", x)
	}
}
