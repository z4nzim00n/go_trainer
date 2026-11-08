package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	var shift int
	fmt.Sscanf(scanner.Text(), "%d", &shift)
	scanner.Scan()
	line := scanner.Text()

	shift = ((shift % 26) + 26) % 26
	encoded := make([]rune, 0, len(line))
	for _, r := range line {
		switch {
		case r >= 'a' && r <= 'z':
			encoded = append(encoded, 'a'+(r-'a'+rune(shift))%26)
		case r >= 'A' && r <= 'Z':
			encoded = append(encoded, 'A'+(r-'A'+rune(shift))%26)
		default:
			encoded = append(encoded, r)
		}
	}
	fmt.Println(string(encoded))
}
