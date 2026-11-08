package main

import (
	"fmt"
	"strconv"
)

func main() {
	var s string
	fmt.Scan(&s)
	n, err := strconv.Atoi(s)
	// TODO: выведи число или сообщение об ошибке
	_ = n
	_ = err
	fmt.Println("TODO")
}
