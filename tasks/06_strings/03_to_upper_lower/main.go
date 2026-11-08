package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	first := scanner.Text()
	scanner.Scan()
	second := scanner.Text()
	// TODO: выведи первую строку в верхнем регистре, вторую — в нижнем
	_, _ = first, second
	fmt.Println("TODO")
}
