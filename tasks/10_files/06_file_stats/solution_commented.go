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

	bytes := len(data)
	// Убираем последний \n, иначе a\nb\n даст три строки.
	text := strings.TrimSuffix(string(data), "\n")
	lines := 0
	if text != "" {
		lines = len(strings.Split(text, "\n"))
	}
	fmt.Printf("Lines: %d\n", lines)
	fmt.Printf("Bytes: %d\n", bytes)
}
