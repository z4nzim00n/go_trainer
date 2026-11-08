package main

import (
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	data, _ := io.ReadAll(os.Stdin)
	line := strings.TrimSpace(string(data))
	// TODO: посчитай слова и выведи по алфавиту
	_ = line
	fmt.Println("TODO")
}
