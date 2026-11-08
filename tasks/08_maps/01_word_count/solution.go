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
	line := strings.TrimSpace(string(data))
	counts := make(map[string]int)
	for _, w := range strings.Fields(line) {
		counts[w]++
	}
	keys := make([]string, 0, len(counts))
	for k := range counts {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	for _, k := range keys {
		fmt.Printf("%s: %d\n", k, counts[k])
	}
}
