package main

import (
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	// Читаем весь ввод: слова могут быть разделены и переводами строк.
	data, _ := io.ReadAll(os.Stdin)
	// Fields игнорирует повторные пробелы и не даёт пустых слов.
	words := strings.Fields(string(data))
	fmt.Println(len(words))
}
