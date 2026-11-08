package main

import "fmt"

func main() {
	var x float64
	fmt.Scan(&x)
	// %.2f — два знака после точки, округление стандартное.
	fmt.Printf("Value: %.2f\n", x)
}
