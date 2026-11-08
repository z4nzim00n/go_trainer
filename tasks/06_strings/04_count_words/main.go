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
		// TODO: посчитай слова и выведи их количество
		_ = line
	}
	fmt.Println("TODO")
}
