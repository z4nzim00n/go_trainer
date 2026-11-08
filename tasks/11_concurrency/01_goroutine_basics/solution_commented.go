package main

import "fmt"

func main() {
	start := make(chan struct{})
	done := make(chan struct{})

	go func() {
		<-start // ждём разрешения
		fmt.Println("worker")
		close(done) // сообщаем, что закончили
	}()

	fmt.Println("main")
	close(start)
	<-done // главная горутина ждёт worker
	fmt.Println("finished")
}
