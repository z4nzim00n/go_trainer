package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		line := scanner.Text()
		// TODO: выведи "Line: " и строку line
		_ = line
	}
	fmt.Println("TODO")
}
