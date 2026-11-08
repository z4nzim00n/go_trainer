package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var name string
	fmt.Scan(&name)
	data, err := os.ReadFile(name)
	if err != nil {
		fmt.Println("Error: cannot read file")
		return
	}
	// Fields игнорирует повторные пробелы и переводы строк.
	words := strings.Fields(string(data))
	fmt.Printf("Words: %d\n", len(words))
}
