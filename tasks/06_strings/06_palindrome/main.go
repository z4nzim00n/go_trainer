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
		// TODO: проверь палиндром и выведи true/false
		_ = s
	}
	fmt.Println("TODO")
}
