package main

import "fmt"

func process(word string) {
	// close выполнится последним, когда process завершится.
	defer fmt.Println("close")
	fmt.Println("open " + word)
	fmt.Println("work")
}

func main() {
	var word string
	fmt.Scan(&word)
	process(word)
}
