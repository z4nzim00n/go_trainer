package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var name, word string
	fmt.Scan(&name, &word)
	content := word + "\n"
	if err := os.WriteFile(name, []byte(content), 0644); err != nil {
		fmt.Println("Error: cannot write file")
		return
	}
	data, err := os.ReadFile(name)
	if err != nil {
		fmt.Println("Error: cannot read file")
		return
	}
	fmt.Println("Saved: " + strings.TrimSpace(string(data)))
}
