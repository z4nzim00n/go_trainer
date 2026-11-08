package main

import "fmt"

func main() {
	start := make(chan struct{})
	done := make(chan struct{})
	go func() {
		<-start
		fmt.Println("worker")
		close(done)
	}()
	fmt.Println("main")
	close(start)
	<-done
	fmt.Println("finished")
}
