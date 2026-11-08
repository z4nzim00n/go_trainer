package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// Для отрицательных чисел работаем с модулем.
	if n < 0 {
		n = -n
	}
	sum := 0
	for n > 0 {
		sum += n % 10 // последняя цифра
		n /= 10       // отбрасываем её
	}
	fmt.Println(sum)
}
