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
		// TODO: выведи количество символов (рун) в строке
		_ = s
	}
	fmt.Println("TODO")
}
