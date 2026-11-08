package main

import (
	"fmt"
	"os"
	"strconv"
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

	sum := 0
	// Fields сам разбирается с пробелами и переводами строк.
	for _, field := range strings.Fields(string(data)) {
		n, err := strconv.Atoi(field)
		if err != nil {
			continue
		}
		sum += n
	}
	fmt.Printf("Sum: %d\n", sum)
}
