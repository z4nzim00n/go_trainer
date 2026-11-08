package main

import "fmt"

type Point struct {
	X int
	Y int
}

func main() {
	var p Point
	fmt.Scan(&p.X, &p.Y)
	fmt.Printf("X: %d\n", p.X)
	fmt.Printf("Y: %d\n", p.Y)
}
