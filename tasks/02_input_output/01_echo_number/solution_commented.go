package main

import "fmt"

func main() {
	var n int
	// &n — адрес переменной, куда Scan запишет число.
	fmt.Scan(&n)
	fmt.Println(n)
}
