package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	first := scanner.Text()
	scanner.Scan()
	second := scanner.Text()
	// Строки неизменяемы: ToUpper/ToLower возвращают новые значения.
	fmt.Println(strings.ToUpper(first))
	fmt.Println(strings.ToLower(second))
}
