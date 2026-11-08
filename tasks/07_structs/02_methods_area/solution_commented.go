package main

import "fmt"

type Rectangle struct {
	Width  float64
	Height float64
}

// Area — метод с получателем-значением: структура не меняется.
func (r Rectangle) Area() float64 {
	return r.Width * r.Height
}

func main() {
	var r Rectangle
	fmt.Scan(&r.Width, &r.Height)
	fmt.Printf("Area: %.2f\n", r.Area())
}
