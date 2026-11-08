package main

import "fmt"

// Point — точка на плоскости.
type Point struct {
	X int
	Y int
}

func main() {
	var p Point
	// Scan принимает указатели на поля.
	fmt.Scan(&p.X, &p.Y)
	fmt.Printf("X: %d\n", p.X)
	fmt.Printf("Y: %d\n", p.Y)
}
