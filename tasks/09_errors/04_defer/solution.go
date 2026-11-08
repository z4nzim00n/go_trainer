package main

import "fmt"

func process(word string) {
	defer fmt.Println("close")
	fmt.Println("open " + word)
	fmt.Println("work")
}

func main() {
	var word string
	fmt.Scan(&word)
	process(word)
}
