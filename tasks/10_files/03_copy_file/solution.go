package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var src, dst string
	fmt.Scan(&src, &dst)
	data, err := os.ReadFile(src)
	if err != nil {
		fmt.Println("Error: cannot read source")
		return
	}
	if err := os.WriteFile(dst, data, 0644); err != nil {
		fmt.Println("Error: cannot write destination")
		return
	}
	fmt.Printf("Copied: %s\n", strings.TrimSpace(string(data)))
}
