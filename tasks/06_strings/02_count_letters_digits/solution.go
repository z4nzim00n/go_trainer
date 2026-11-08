package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		s := scanner.Text()
		letters := 0
		digits := 0
		for _, r := range s {
			if unicode.IsLetter(r) {
				letters++
			}
			if unicode.IsDigit(r) {
				digits++
			}
		}
		fmt.Printf("%d %d\n", letters, digits)
	}
}
