package main

import "fmt"

type Rectangle struct {
	Width  float64
	Height float64
}

func (r Rectangle) Area() float64 {
	return r.Width * r.Height
}

func main() {
	var r Rectangle
	fmt.Scan(&r.Width, &r.Height)
	fmt.Printf("Area: %.2f\n", r.Area())
}
