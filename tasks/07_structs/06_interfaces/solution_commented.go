package main

import (
	"fmt"
	"math"
)

// Shape — всё, у чего есть площадь.
type Shape interface {
	Area() float64
}

type Circle struct{ R float64 }

type Square struct{ Side float64 }

func (c Circle) Area() float64 {
	return math.Pi * c.R * c.R
}

func (s Square) Area() float64 {
	return s.Side * s.Side
}

func main() {
	var r, side float64
	fmt.Scan(&r, &side)
	// В срезе интерфейсов могут лежать значения разных типов.
	shapes := []Shape{Circle{R: r}, Square{Side: side}}
	total := 0.0
	for _, s := range shapes {
		total += s.Area()
	}
	fmt.Printf("Total: %.2f\n", total)
}
