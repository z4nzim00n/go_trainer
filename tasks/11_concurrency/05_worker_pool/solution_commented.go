package main

import (
	"fmt"
	"sync"
)

func main() {
	var n int
	fmt.Scan(&n)

	jobs := make(chan int)
	results := make(chan int)
	var wg sync.WaitGroup

	// Три воркера читают одну очередь jobs.
	for i := 0; i < 3; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for j := range jobs {
				results <- j * j
			}
		}()
	}

	go func() {
		for i := 1; i <= n; i++ {
			jobs <- i
		}
		close(jobs)
		wg.Wait()      // ждём, пока воркеры дочитают jobs
		close(results) // только теперь можно закрывать результаты
	}()

	total := 0
	for r := range results {
		total += r
	}
	fmt.Printf("Total: %d\n", total)
}
