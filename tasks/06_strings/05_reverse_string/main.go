package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		s := scanner.Text()
		// TODO: разверни строку по символам и выведи результат
		_ = s
	}
	fmt.Println("TODO")
}
