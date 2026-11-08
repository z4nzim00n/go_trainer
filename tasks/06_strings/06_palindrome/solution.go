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
		normalized := make([]rune, 0, len(s))
		for _, r := range s {
			if unicode.IsLetter(r) || unicode.IsDigit(r) {
				normalized = append(normalized, unicode.ToLower(r))
			}
		}
		ok := true
		for i, j := 0, len(normalized)-1; i < j; i, j = i+1, j-1 {
			if normalized[i] != normalized[j] {
				ok = false
				break
			}
		}
		fmt.Println(ok)
	}
}
