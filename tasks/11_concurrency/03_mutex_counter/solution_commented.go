package main

import (
	"fmt"
	"sync"
)

func main() {
	var n int
	fmt.Scan(&n)

	var mu sync.Mutex
	var wg sync.WaitGroup
	counter := 0

	for i := 0; i < n; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for j := 0; j < 1000; j++ {
				// Только одна горутина меняет counter в этот момент.
				mu.Lock()
				counter++
				mu.Unlock()
			}
		}()
	}

	wg.Wait()
	fmt.Printf("Counter: %d\n", counter)
}
