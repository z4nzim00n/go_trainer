package main

import "fmt"

// TODO: объяви интерфейс Shape

type Shape interface {
	Area() float64
}

type Circle struct{ R float64 }

type Square struct{ Side float64 }

// TODO: реализуй Area для обеих фигур
func (c Circle) Area() float64 { return 0 }

func (s Square) Area() float64 { return 0 }

func main() {
	var r, side float64
	fmt.Scan(&r, &side)
	shapes := []Shape{Circle{R: r}, Square{Side: side}}
	total := 0.0
	for _, s := range shapes {
		total += s.Area()
	}
	fmt.Printf("Total: %.2f\n", total)
}
