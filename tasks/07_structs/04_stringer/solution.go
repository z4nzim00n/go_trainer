package main

import "fmt"

type Temperature float64

func (t Temperature) String() string {
	return fmt.Sprintf("%.2f°C", float64(t))
}

func main() {
	var t Temperature
	fmt.Scan(&t)
	fmt.Printf("Temp: %v\n", t)
}
