package main

import (
	"fmt"
	"os"
)

func main() {
	var name string
	fmt.Scan(&name)
	data, err := os.ReadFile(name)
	if err != nil {
		fmt.Println("Error: cannot read file")
		return
	}
	fmt.Print(string(data))
}
