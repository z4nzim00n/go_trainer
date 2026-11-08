package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode/utf8"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		s := scanner.Text()
		// len(s) — байты, RuneCountInString — символы Unicode.
		fmt.Println(utf8.RuneCountInString(s))
	}
}
