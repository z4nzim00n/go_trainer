package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// divisor — степень десяти, соответствующая старшей цифре.
	divisor := 1
	for n/divisor >= 10 {
		divisor *= 10
	}
	first := n / divisor
	last := n % 10
	middle := (n % divisor) / 10
	// Собираем число: последняя цифра, середина, первая цифра.
	result := last*divisor + middle*10 + first
	fmt.Println(result)
}
