@@TASK
section: 11_concurrency
dir: 01_goroutine_basics
num: 11_1
title: GO_11_01. Первая горутина
topics: `go`, каналы, синхронизация
input: Ввод не нужен
@@DESC
Запусти горутину, которая печатает `worker`. Главная функция печатает `main`,
дожидается горутины через канал и печатает `finished`.

~~~text
main
worker
finished
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| *(нет)* | main<br>worker<br>finished |
@@THEORY
## Горутина

~~~go
go func() {
    fmt.Println("worker")
}()
~~~

`go` запускает функцию параллельно. Главная горутина при этом продолжает
работу и может завершиться раньше — тогда программа закончится.

## Канал для ожидания

~~~go
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
~~~

`struct{}` — пустой тип, он ничего не занимает. Такой канал используют только
как сигнал.

## Гонка

Без синхронизации порядок вывода `main` и `worker` не определён. Канал
делает порядок предсказуемым.
@@TESTS
| *(нет)* | `main\nworker\nfinished\n` |
@@CASES
run_case "" $'main\nworker\nfinished\n'
@@MAIN
package main

import "fmt"

func main() {
	// TODO: запусти горутину и дождись её через канал
	fmt.Println("TODO")
}
@@SOLUTION
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
@@COMMENTED
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
@@END

@@TASK
section: 11_concurrency
dir: 02_two_goroutines
num: 11_2
title: GO_11_02. Две горутины
topics: каналы, буферизация, суммирование
input: Два целых числа A и B
@@DESC
Запусти две горутины: первая удваивает `A`, вторая удваивает `B`.
Результаты приходят через канал. Выведи сумму:

~~~text
Sum: 14
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 3 4 | Sum: 14 |
| 0 5 | Sum: 10 |
@@THEORY
## Буферизованный канал

~~~go
ch := make(chan int, 2)
go func() { ch <- a * 2 }()
go func() { ch <- b * 2 }()
sum := <-ch + <-ch
~~~

Буфер на 2 элемента позволяет обеим горутинам отправить результат, даже если
главная ещё не читает.

## Без буфера

С небуферизованным каналом отправка блокируется до чтения. Тоже работает:
главная горутина прочитает оба значения.

## Порядок

Кто из горутин отправит первым — неизвестно. Для суммы порядок не важен,
поэтому результат стабилен.
@@TESTS
| `3 4` | `Sum: 14\n` |
| `0 5` | `Sum: 10\n` |
| `-1 2` | `Sum: 2\n` |
@@CASES
run_case "3 4" $'Sum: 14\n'
run_case "0 5" $'Sum: 10\n'
run_case "-1 2" $'Sum: 2\n'
@@MAIN
package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	// TODO: запусти две горутины и сложи результаты
	_ = a
	_ = b
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	ch := make(chan int, 2)
	go func() { ch <- a * 2 }()
	go func() { ch <- b * 2 }()
	sum := <-ch + <-ch
	fmt.Printf("Sum: %d\n", sum)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)

	// Буфер на 2 значения: обе горутины смогут отправить результат.
	ch := make(chan int, 2)
	go func() { ch <- a * 2 }()
	go func() { ch <- b * 2 }()

	// Читаем два значения; порядок не важен для суммы.
	sum := <-ch + <-ch
	fmt.Printf("Sum: %d\n", sum)
}
@@END

@@TASK
section: 11_concurrency
dir: 03_mutex_counter
num: 11_3
title: GO_11_03. Счётчик с Mutex
topics: `sync.Mutex`, `sync.WaitGroup`, гонки данных
input: Число горутин N
@@DESC
Запусти `N` горутин. Каждая увеличивает общий счётчик 1000 раз.
Защити счётчик через `sync.Mutex` и дождись всех через `sync.WaitGroup`.
Выведи итог:

~~~text
Counter: 4000
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 4 | Counter: 4000 |
| 1 | Counter: 1000 |
| 0 | Counter: 0 |
@@THEORY
## Гонка данных

~~~go
counter++ // не атомарная операция
~~~

Две горутины могут прочитать одно и то же значение и потерять одно из
приращений. Результат будет меньше ожидаемого.

## Mutex

~~~go
var mu sync.Mutex
mu.Lock()
counter++
mu.Unlock()
~~~

`Lock` пропускает только одну горутину в критическую секцию.

## WaitGroup

~~~go
var wg sync.WaitGroup
wg.Add(1)
go func() {
    defer wg.Done()
    // работа
}()
wg.Wait()
~~~

`Add` сообщает, сколько горутин ждать, `Done` уменьшает счётчик, `Wait`
блокируется до нуля.

## Проверка гонок

~~~bash
go run -race main.go
~~~

Флаг `-race` находит обращения к общей памяти без синхронизации.
@@TESTS
| `4` | `Counter: 4000\n` |
| `1` | `Counter: 1000\n` |
| `0` | `Counter: 0\n` |
| `3` | `Counter: 3000\n` |
@@CASES
run_case "4" $'Counter: 4000\n'
run_case "1" $'Counter: 1000\n'
run_case "0" $'Counter: 0\n'
run_case "3" $'Counter: 3000\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// TODO: запусти n горутин с mutex и WaitGroup
	_ = n
	fmt.Println("TODO")
}
@@SOLUTION
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
				mu.Lock()
				counter++
				mu.Unlock()
			}
		}()
	}

	wg.Wait()
	fmt.Printf("Counter: %d\n", counter)
}
@@COMMENTED
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
@@END

@@TASK
section: 11_concurrency
dir: 04_channel_pipeline
num: 11_4
title: GO_11_04. Конвейер каналов
topics: конвейер, `range` по каналу, `close`
input: Число N, затем N целых чисел
@@DESC
Построй конвейер из двух стадий:
1. генератор отправляет числа в канал;
2. вторая стадия возводит каждое число в квадрат.

Главная функция суммирует квадраты и выводит `Sum: ...`.

~~~text
Sum: 14
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 3<br>1 2 3 | Sum: 14 |
| 2<br>2 4 | Sum: 20 |
| 0 | Sum: 0 |
@@THEORY
## Стадии конвейера

~~~go
func square(in <-chan int) <-chan int {
    out := make(chan int)
    go func() {
        for x := range in {
            out <- x * x
        }
        close(out)
    }()
    return out
}
~~~

Каждая стадия — горутина, читающая из входного канала и пишущая в выходной.

## Закрытие канала

`close(out)` сообщает читателю, что значений больше не будет. `range` по
каналу завершается после закрытия.

## Направления каналов

~~~go
func square(in <-chan int) <-chan int
~~~

`<-chan` — только читать, `chan<-` — только писать. Компилятор проверяет
направление.
@@TESTS
| `3\n1 2 3` | `Sum: 14\n` |
| `2\n2 4` | `Sum: 20\n` |
| `0` | `Sum: 0\n` |
| `4\n1 1 1 1` | `Sum: 4\n` |
@@CASES
run_case $'3\n1 2 3' $'Sum: 14\n'
run_case $'2\n2 4' $'Sum: 20\n'
run_case "0" $'Sum: 0\n'
run_case $'4\n1 1 1 1' $'Sum: 4\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	values := make([]int, n)
	for i := range values {
		fmt.Scan(&values[i])
	}
	// TODO: собери конвейер и посчитай сумму квадратов
	_ = values
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	values := make([]int, n)
	for i := range values {
		fmt.Scan(&values[i])
	}

	in := make(chan int)
	out := make(chan int)

	go func() {
		for _, x := range values {
			in <- x
		}
		close(in)
	}()

	go func() {
		for x := range in {
			out <- x * x
		}
		close(out)
	}()

	sum := 0
	for x := range out {
		sum += x
	}
	fmt.Printf("Sum: %d\n", sum)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	values := make([]int, n)
	for i := range values {
		fmt.Scan(&values[i])
	}

	in := make(chan int)
	out := make(chan int)

	// Стадия 1: генератор.
	go func() {
		for _, x := range values {
			in <- x
		}
		close(in)
	}()

	// Стадия 2: квадраты. Закрывает out, когда in опустеет.
	go func() {
		for x := range in {
			out <- x * x
		}
		close(out)
	}()

	// Главная горутина читает результаты.
	sum := 0
	for x := range out {
		sum += x
	}
	fmt.Printf("Sum: %d\n", sum)
}
@@END

@@TASK
section: 11_concurrency
dir: 05_worker_pool
num: 11_5
title: GO_11_05. Пул воркеров
topics: пул горутин, `WaitGroup`, `close`
input: Число N
@@DESC
Создай 3 воркера и отправь им числа от `1` до `N`. Каждый воркер
возводит число в квадрат и возвращает результат. Суммируй результаты
и выведи `Total: ...`.

~~~text
Total: 55
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 5 | Total: 55 |
| 3 | Total: 14 |
| 0 | Total: 0 |
@@THEORY
## Пул воркеров

~~~go
jobs := make(chan int)
results := make(chan int)
var wg sync.WaitGroup

for i := 0; i < 3; i++ {
    wg.Add(1)
    go func() {
        defer wg.Done()
        for j := range jobs {
            results <- j * j
        }
    }()
}
~~~

Все воркеры читают из одного канала `jobs` — работа распределяется
автоматически.

## Завершение

~~~go
go func() {
    for i := 1; i <= n; i++ {
        jobs <- i
    }
    close(jobs)
    wg.Wait()
    close(results)
}()
~~~

Сначала закрываем `jobs`, затем ждём воркеров, и только потом закрываем
`results`. Если закрыть `results` раньше, воркеры запаникуют.

## Почему пул

Создавать горутину на каждую задачу накладно. Пул ограничивает число
одновременных работников.
@@TESTS
| `5` | `Total: 55\n` |
| `3` | `Total: 14\n` |
| `0` | `Total: 0\n` |
| `10` | `Total: 385\n` |
@@CASES
run_case "5" $'Total: 55\n'
run_case "3" $'Total: 14\n'
run_case "0" $'Total: 0\n'
run_case "10" $'Total: 385\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// TODO: сделай пул из 3 воркеров
	_ = n
	fmt.Println("TODO")
}
@@SOLUTION
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
		wg.Wait()
		close(results)
	}()

	total := 0
	for r := range results {
		total += r
	}
	fmt.Printf("Total: %d\n", total)
}
@@COMMENTED
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
@@END

@@TASK
section: 12_bootcamp
dir: 01_prime_check
num: 12_1
title: GO_12_01. Проверка на простое число
topics: циклы, `math.Sqrt`, ранний выход
input: Одно целое число
@@DESC
Определи, является ли число простым. Выведи `Prime` или `Not prime`.

~~~text
Prime
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 17 | Prime |
| 9 | Not prime |
| 1 | Not prime |
@@THEORY
## Простое число

Простое число больше `1` и делится только на `1` и на себя.

## Перебор делителей

~~~go
func isPrime(n int) bool {
    if n < 2 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}
~~~

Проверять делители достаточно до `i*i <= n`: если есть делитель больше
корня, то есть и меньше корня.

## Ранний выход

`return false` внутри цикла прекращает проверку, как только найден делитель.

## Отрицательные числа

`n < 2` отсекает и `0`, и `1`, и отрицательные значения.
@@TESTS
| `17` | `Prime\n` |
| `9` | `Not prime\n` |
| `1` | `Not prime\n` |
| `2` | `Prime\n` |
| `-5` | `Not prime\n` |
| `97` | `Prime\n` |
@@CASES
run_case "17" $'Prime\n'
run_case "9" $'Not prime\n'
run_case "1" $'Not prime\n'
run_case "2" $'Prime\n'
run_case "-5" $'Not prime\n'
run_case "97" $'Prime\n'
@@MAIN
package main

import "fmt"

func isPrime(n int) bool {
	// TODO: реализуй проверку
	return false
}

func main() {
	var n int
	fmt.Scan(&n)
	if isPrime(n) {
		fmt.Println("Prime")
	} else {
		fmt.Println("Not prime")
	}
}
@@SOLUTION
package main

import "fmt"

func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	var n int
	fmt.Scan(&n)
	if isPrime(n) {
		fmt.Println("Prime")
	} else {
		fmt.Println("Not prime")
	}
}
@@COMMENTED
package main

import "fmt"

func isPrime(n int) bool {
	// 0, 1 и отрицательные числа не простые.
	if n < 2 {
		return false
	}
	// Достаточно проверить делители до sqrt(n).
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	var n int
	fmt.Scan(&n)
	if isPrime(n) {
		fmt.Println("Prime")
	} else {
		fmt.Println("Not prime")
	}
}
@@END

@@TASK
section: 12_bootcamp
dir: 02_coffee_machine
num: 12_2
title: GO_12_02. Кофейный автомат
topics: накопление, условия, форматирование
input: Число монет N, затем N номиналов
@@DESC
Кофе стоит 50. Считай `N` монет и их номиналы.
Если сумма не меньше 50, выведи `Coffee: <сдача>`, иначе `Need: <недостаёт>`.

~~~text
Coffee: 10
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 3<br>20 20 20 | Coffee: 10 |
| 1<br>20 | Need: 30 |
| 2<br>50 10 | Coffee: 10 |
@@THEORY
## Накопление

~~~go
total := 0
for i := 0; i < n; i++ {
    var coin int
    fmt.Scan(&coin)
    total += coin
}
~~~

## Ветвление

~~~go
const price = 50
if total >= price {
    fmt.Printf("Coffee: %d\n", total-price)
} else {
    fmt.Printf("Need: %d\n", price-total)
}
~~~

`const` объявляет неизменяемую константу.

## Точное равенство

Случай `total == 50` попадает в первую ветку: сдача `0`. Проверяй границу
явно — это классическая ошибка `>` вместо `>=`.
@@TESTS
| `3\n20 20 20` | `Coffee: 10\n` |
| `1\n20` | `Need: 30\n` |
| `2\n50 10` | `Coffee: 10\n` |
| `0` | `Need: 50\n` |
@@CASES
run_case $'3\n20 20 20' $'Coffee: 10\n'
run_case $'1\n20' $'Need: 30\n'
run_case $'2\n50 10' $'Coffee: 10\n'
run_case "0" $'Need: 50\n'
@@MAIN
package main

import "fmt"

const price = 50

func main() {
	var n int
	fmt.Scan(&n)
	total := 0
	for i := 0; i < n; i++ {
		var coin int
		fmt.Scan(&coin)
		total += coin
	}
	// TODO: реши, хватает ли денег
	_ = total
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

const price = 50

func main() {
	var n int
	fmt.Scan(&n)
	total := 0
	for i := 0; i < n; i++ {
		var coin int
		fmt.Scan(&coin)
		total += coin
	}
	if total >= price {
		fmt.Printf("Coffee: %d\n", total-price)
	} else {
		fmt.Printf("Need: %d\n", price-total)
	}
}
@@COMMENTED
package main

import "fmt"

const price = 50

func main() {
	var n int
	fmt.Scan(&n)
	total := 0
	for i := 0; i < n; i++ {
		var coin int
		fmt.Scan(&coin)
		total += coin
	}
	// Граница total == price тоже считается успехом.
	if total >= price {
		fmt.Printf("Coffee: %d\n", total-price)
	} else {
		fmt.Printf("Need: %d\n", price-total)
	}
}
@@END

@@TASK
section: 12_bootcamp
dir: 03_statistics
num: 12_3
title: GO_12_03. Статистика
topics: минимум, максимум, среднее
input: Число N, затем N целых чисел
@@DESC
Выведи минимум, максимум и среднее арифметическое:

~~~text
Min: 1
Max: 9
Avg: 4.33
~~~

Если `N = 0`, все три значения — нули.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 3<br>1 5 7 | Min: 1<br>Max: 7<br>Avg: 4.33 |
| 0 | Min: 0<br>Max: 0<br>Avg: 0.00 |
@@THEORY
## Начальные значения

~~~go
min := numbers[0]
max := numbers[0]
sum := 0
for _, x := range numbers {
    if x < min { min = x }
    if x > max { max = x }
    sum += x
}
~~~

Нельзя начинать `min` с `0`: все числа могут быть положительными, и тогда
`0` останется минимумом.

## Среднее

~~~go
avg := float64(sum) / float64(n)
~~~

Приводим оба числа к `float64`, иначе произойдёт целочисленное деление.

## Пустой срез

Обращение `numbers[0]` при `n == 0` паникует. Пустой ввод обрабатываем
до цикла.
@@TESTS
| `3\n1 5 7` | `Min: 1\nMax: 7\nAvg: 4.33\n` |
| `0` | `Min: 0\nMax: 0\nAvg: 0.00\n` |
| `1\n5` | `Min: 5\nMax: 5\nAvg: 5.00\n` |
| `4\n-2 4 0 2` | `Min: -2\nMax: 4\nAvg: 1.00\n` |
@@CASES
run_case $'3\n1 5 7' $'Min: 1\nMax: 7\nAvg: 4.33\n'
run_case "0" $'Min: 0\nMax: 0\nAvg: 0.00\n'
run_case $'1\n5' $'Min: 5\nMax: 5\nAvg: 5.00\n'
run_case $'4\n-2 4 0 2' $'Min: -2\nMax: 4\nAvg: 1.00\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	numbers := make([]int, n)
	for i := range numbers {
		fmt.Scan(&numbers[i])
	}
	// TODO: посчитай min, max и avg
	_ = numbers
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	if n == 0 {
		fmt.Println("Min: 0")
		fmt.Println("Max: 0")
		fmt.Println("Avg: 0.00")
		return
	}
	numbers := make([]int, n)
	for i := range numbers {
		fmt.Scan(&numbers[i])
	}
	min, max, sum := numbers[0], numbers[0], 0
	for _, x := range numbers {
		if x < min {
			min = x
		}
		if x > max {
			max = x
		}
		sum += x
	}
	fmt.Printf("Min: %d\n", min)
	fmt.Printf("Max: %d\n", max)
	fmt.Printf("Avg: %.2f\n", float64(sum)/float64(n))
}
@@COMMENTED
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	if n == 0 {
		fmt.Println("Min: 0")
		fmt.Println("Max: 0")
		fmt.Println("Avg: 0.00")
		return
	}

	numbers := make([]int, n)
	for i := range numbers {
		fmt.Scan(&numbers[i])
	}

	// Начинаем с первого элемента, а не с нуля.
	min, max, sum := numbers[0], numbers[0], 0
	for _, x := range numbers {
		if x < min {
			min = x
		}
		if x > max {
			max = x
		}
		sum += x
	}
	fmt.Printf("Min: %d\n", min)
	fmt.Printf("Max: %d\n", max)
	fmt.Printf("Avg: %.2f\n", float64(sum)/float64(n))
}
@@END

@@TASK
section: 12_bootcamp
dir: 04_histogram
num: 12_4
title: GO_12_04. Гистограмма
topics: `map`, `strings.Repeat`, диапазон значений
input: Число N, затем N чисел от 1 до 9
@@DESC
Построй горизонтальную гистограмму: для каждого встреченного значения
выведи `значение: ***`, где количество звёздочек равно частоте. Значения
идут по возрастанию.

~~~text
1: **
2: *
3: **
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 5<br>1 2 1 3 3 | 1: **<br>2: *<br>3: ** |
| 0 | *(пусто)* |
@@THEORY
## Подсчёт частот

~~~go
counts := make(map[int]int)
for i := 0; i < n; i++ {
    var x int
    fmt.Scan(&x)
    counts[x]++
}
~~~

## Звёздочки

~~~go
fmt.Printf("%d: %s\n", value, strings.Repeat("*", counts[value]))
~~~

`strings.Repeat` создаёт строку из повторённого фрагмента.

## Диапазон

Если значения лежат в `1..9`, можно пройти циклом по всем числам и напечатать
только встреченные. Так порядок гарантированно возрастает.

~~~go
for v := 1; v <= maxValue; v++ {
    if counts[v] == 0 {
        continue
    }
    // вывод
}
~~~
@@TESTS
| `5\n1 2 1 3 3` | `1: **\n2: *\n3: **\n` |
| `3\n9 9 9` | `9: ***\n` |
| `0` | *(пусто)* |
@@CASES
run_case $'5\n1 2 1 3 3' $'1: **\n2: *\n3: **\n'
run_case $'3\n9 9 9' $'9: ***\n'
run_case "0" ""
@@MAIN
package main

import (
	"fmt"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	counts := make(map[int]int)
	maxValue := 0
	for i := 0; i < n; i++ {
		var x int
		fmt.Scan(&x)
		counts[x]++
		if x > maxValue {
			maxValue = x
		}
	}
	// TODO: выведи гистограмму по возрастанию
	_ = strings.Repeat
	_ = maxValue
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"fmt"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	counts := make(map[int]int)
	maxValue := 0
	for i := 0; i < n; i++ {
		var x int
		fmt.Scan(&x)
		counts[x]++
		if x > maxValue {
			maxValue = x
		}
	}
	for v := 1; v <= maxValue; v++ {
		if counts[v] == 0 {
			continue
		}
		fmt.Printf("%d: %s\n", v, strings.Repeat("*", counts[v]))
	}
}
@@COMMENTED
package main

import (
	"fmt"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	counts := make(map[int]int)
	maxValue := 0
	for i := 0; i < n; i++ {
		var x int
		fmt.Scan(&x)
		counts[x]++
		if x > maxValue {
			maxValue = x
		}
	}

	// Идём по возрастанию и печатаем только встреченные значения.
	for v := 1; v <= maxValue; v++ {
		if counts[v] == 0 {
			continue
		}
		fmt.Printf("%d: %s\n", v, strings.Repeat("*", counts[v]))
	}
}
@@END

@@TASK
section: 12_bootcamp
dir: 05_rotate_array
num: 12_5
title: GO_12_05. Циклический сдвиг
topics: срезы, `append`, `%`
input: Число N, сдвиг K, затем N целых чисел
@@DESC
Сдвинь массив вправо на `K` позиций (циклически) и выведи через пробел.
`K` может быть больше `N`.

~~~text
4 5 1 2 3
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 5 2<br>1 2 3 4 5 | 4 5 1 2 3 |
| 5 7<br>1 2 3 4 5 | 4 5 1 2 3 |
| 1 3<br>7 | 7 |
@@THEORY
## Сдвиг по модулю

~~~go
k = k % n
~~~

`K = 7` при `N = 5` — то же, что `K = 2`: полный круг возвращает массив
в исходное состояние.

## Разрезание среза

~~~go
result := append([]int{}, a[n-k:]...)
result = append(result, a[:n-k]...)
~~~

`a[n-k:]` — хвост, `a[:n-k]` — начало. Вместе они дают сдвиг вправо.
Копию делаем, чтобы не испортить исходный срез при `append`.

## Крайние случаи

- `n == 0` — выводим пустую строку;
- `k % n == 0` — массив не меняется.
@@TESTS
| `5 2\n1 2 3 4 5` | `4 5 1 2 3\n` |
| `5 7\n1 2 3 4 5` | `4 5 1 2 3\n` |
| `1 3\n7` | `7\n` |
| `4 0\n1 2 3 4` | `1 2 3 4\n` |
| `0 5` | `\n` |
@@CASES
run_case $'5 2\n1 2 3 4 5' $'4 5 1 2 3\n'
run_case $'5 7\n1 2 3 4 5' $'4 5 1 2 3\n'
run_case $'1 3\n7' $'7\n'
run_case $'4 0\n1 2 3 4' $'1 2 3 4\n'
run_case "0 5" $'\n'
@@MAIN
package main

import (
	"fmt"
	"strings"
)

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	a := make([]int, n)
	for i := range a {
		fmt.Scan(&a[i])
	}
	// TODO: сдвинь a вправо на k
	_ = k
	parts := make([]string, len(a))
	for i, x := range a {
		parts[i] = fmt.Sprint(x)
	}
	fmt.Println(strings.Join(parts, " "))
}
@@SOLUTION
package main

import (
	"fmt"
	"strings"
)

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	a := make([]int, n)
	for i := range a {
		fmt.Scan(&a[i])
	}
	if n == 0 {
		fmt.Println()
		return
	}
	k = k % n
	result := append([]int{}, a[n-k:]...)
	result = append(result, a[:n-k]...)
	parts := make([]string, len(result))
	for i, x := range result {
		parts[i] = fmt.Sprint(x)
	}
	fmt.Println(strings.Join(parts, " "))
}
@@COMMENTED
package main

import (
	"fmt"
	"strings"
)

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	a := make([]int, n)
	for i := range a {
		fmt.Scan(&a[i])
	}
	if n == 0 {
		fmt.Println()
		return
	}

	// Полный круг не меняет массив.
	k = k % n
	result := append([]int{}, a[n-k:]...)
	result = append(result, a[:n-k]...)

	parts := make([]string, len(result))
	for i, x := range result {
		parts[i] = fmt.Sprint(x)
	}
	fmt.Println(strings.Join(parts, " "))
}
@@END

@@TASK
section: 12_bootcamp
dir: 06_matrix_sum
num: 12_6
title: GO_12_06. Сумма матрицы
topics: вложенные срезы, двойной цикл
input: Число строк R, число столбцов C, затем R×C чисел
@@DESC
Считай матрицу размера `R × C` и выведи сумму всех элементов:

~~~text
Sum: 21
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 2 3<br>1 2 3<br>4 5 6 | Sum: 21 |
| 1 1<br>7 | Sum: 7 |
| 0 0 | Sum: 0 |
@@THEORY
## Вложенные срезы

~~~go
matrix := make([][]int, rows)
for i := range matrix {
    matrix[i] = make([]int, cols)
    for j := range matrix[i] {
        fmt.Scan(&matrix[i][j])
    }
}
~~~

`make([][]int, rows)` создаёт срез строк, каждую строку нужно создать отдельно.

## Обход

~~~go
sum := 0
for _, row := range matrix {
    for _, x := range row {
        sum += x
    }
}
~~~

Внешний цикл идёт по строкам, внутренний — по элементам строки.

## Почему не make([][]int, rows, cols)

Второй аргумент — длина внешнего среза. Он не задаёт длину вложенных срезов.
@@TESTS
| `2 3\n1 2 3\n4 5 6` | `Sum: 21\n` |
| `1 1\n7` | `Sum: 7\n` |
| `0 0` | `Sum: 0\n` |
| `3 2\n-1 2\n3 4\n5 -6` | `Sum: 7\n` |
@@CASES
run_case $'2 3\n1 2 3\n4 5 6' $'Sum: 21\n'
run_case $'1 1\n7' $'Sum: 7\n'
run_case "0 0" $'Sum: 0\n'
run_case $'3 2\n-1 2\n3 4\n5 -6' $'Sum: 7\n'
@@MAIN
package main

import "fmt"

func main() {
	var rows, cols int
	fmt.Scan(&rows, &cols)
	matrix := make([][]int, rows)
	for i := range matrix {
		matrix[i] = make([]int, cols)
		for j := range matrix[i] {
			fmt.Scan(&matrix[i][j])
		}
	}
	// TODO: посчитай сумму элементов
	_ = matrix
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var rows, cols int
	fmt.Scan(&rows, &cols)
	matrix := make([][]int, rows)
	for i := range matrix {
		matrix[i] = make([]int, cols)
		for j := range matrix[i] {
			fmt.Scan(&matrix[i][j])
		}
	}
	sum := 0
	for _, row := range matrix {
		for _, x := range row {
			sum += x
		}
	}
	fmt.Printf("Sum: %d\n", sum)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var rows, cols int
	fmt.Scan(&rows, &cols)

	matrix := make([][]int, rows)
	for i := range matrix {
		matrix[i] = make([]int, cols)
		for j := range matrix[i] {
			fmt.Scan(&matrix[i][j])
		}
	}

	// Внешний цикл — строки, внутренний — элементы строки.
	sum := 0
	for _, row := range matrix {
		for _, x := range row {
			sum += x
		}
	}
	fmt.Printf("Sum: %d\n", sum)
}
@@END
