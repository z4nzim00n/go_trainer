package main

import (
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	data, _ := io.ReadAll(os.Stdin)
	words := strings.Fields(string(data))
	// TODO: сгруппируй слова по длине
	_ = words
	fmt.Println("TODO")
}
