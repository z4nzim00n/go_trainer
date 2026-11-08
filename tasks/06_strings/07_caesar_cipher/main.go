package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	var shift int
	fmt.Sscanf(scanner.Text(), "%d", &shift)
	scanner.Scan()
	line := scanner.Text()
	// TODO: зашифруй line сдвигом shift и выведи результат
	_ = line
	fmt.Println("TODO")
}
