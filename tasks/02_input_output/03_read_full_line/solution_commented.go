package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// Scanner читает строку целиком до \n.
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		fmt.Println("Line: " + scanner.Text())
	}
}
