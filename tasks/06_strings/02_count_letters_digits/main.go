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
		// TODO: посчитай буквы и цифры и выведи "letters digits"
		_ = s
	}
	fmt.Println("TODO")
}
