package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	direct := make(map[string]int)
	for i := 0; i < n; i++ {
		var word string
		var num int
		fmt.Scan(&word, &num)
		direct[word] = num
	}
	// TODO: построй обратную map и выведи по возрастанию числа
	_ = direct
	fmt.Println("TODO")
}
