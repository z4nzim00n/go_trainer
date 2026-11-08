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
	fmt.Println(len(words))
}
