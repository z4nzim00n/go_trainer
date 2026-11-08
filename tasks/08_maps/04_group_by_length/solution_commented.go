package main

import (
	"fmt"
	"io"
	"os"
	"sort"
	"strings"
)

func main() {
	data, _ := io.ReadAll(os.Stdin)
	words := strings.Fields(string(data))

	// Ключ — длина слова, значение — срез слов этой длины.
	groups := make(map[int][]string)
	for _, w := range words {
		n := len([]rune(w))
		groups[n] = append(groups[n], w)
	}

	lengths := make([]int, 0, len(groups))
	for n := range groups {
		lengths = append(lengths, n)
	}
	sort.Ints(lengths)

	for _, n := range lengths {
		sort.Strings(groups[n])
		fmt.Printf("%d: %s\n", n, strings.Join(groups[n], " "))
	}
}
