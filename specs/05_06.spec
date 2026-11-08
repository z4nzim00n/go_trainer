@@TASK
section: 05_slices
dir: 01_slice_sum_average
num: 5_1
title: GO_05_01. Сумма и среднее
topics: срезы, `append`, `len`, `float64`
input: Число N, затем N целых чисел
@@DESC
Считай `N`, затем `N` чисел. Выведи сумму и среднее:

~~~text
Sum: 6
Avg: 2.00
~~~

Если `N = 0`, сумма и среднее равны нулю.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 3<br>1 2 3 | Sum: 6<br>Avg: 2.00 |
| 1<br>5 | Sum: 5<br>Avg: 5.00 |
| 0 | Sum: 0<br>Avg: 0.00 |
@@THEORY
## Срез

~~~go
numbers := make([]int, 0, n)
for i := 0; i < n; i++ {
    var x int
    fmt.Scan(&x)
    numbers = append(numbers, x)
}
~~~

Срез — динамическая последовательность. `append` добавляет элемент и при
необходимости расширяет массив.

## Сумма

~~~go
sum := 0
for _, x := range numbers {
    sum += x
}
~~~

`_` — пустой идентификатор: индекс нам не нужен.

## Среднее

~~~go
avg := 0.0
if n > 0 {
    avg = float64(sum) / float64(n)
}
~~~

Деление на ноль для `float64` дало бы `NaN`, поэтому пустой ввод обрабатываем
отдельно.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `sum / n` | Целочисленное деление |
| Нет проверки `n == 0` | `NaN` вместо `0.00` |
| `numbers[i] = x` без `make` | Паника: индекс вне диапазона |
@@TESTS
| `3` + `1 2 3` | `Sum: 6\nAvg: 2.00\n` |
| `1` + `5` | `Sum: 5\nAvg: 5.00\n` |
| `0` | `Sum: 0\nAvg: 0.00\n` |
| `4` + `-2 4 0 2` | `Sum: 4\nAvg: 1.00\n` |
@@CASES
run_case $'3\n1 2 3' $'Sum: 6\nAvg: 2.00\n'
run_case $'1\n5' $'Sum: 5\nAvg: 5.00\n'
run_case "0" $'Sum: 0\nAvg: 0.00\n'
run_case $'4\n-2 4 0 2' $'Sum: 4\nAvg: 1.00\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	numbers := make([]int, 0, n)
	for i := 0; i < n; i++ {
		var x int
		fmt.Scan(&x)
		numbers = append(numbers, x)
	}
	// TODO: посчитай сумму и среднее и выведи Sum/Avg
	_ = numbers
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	numbers := make([]int, 0, n)
	for i := 0; i < n; i++ {
		var x int
		fmt.Scan(&x)
		numbers = append(numbers, x)
	}
	sum := 0
	for _, x := range numbers {
		sum += x
	}
	avg := 0.0
	if n > 0 {
		avg = float64(sum) / float64(n)
	}
	fmt.Printf("Sum: %d\n", sum)
	fmt.Printf("Avg: %.2f\n", avg)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// Срез с запасом ёмкости: append не будет перевыделять память.
	numbers := make([]int, 0, n)
	for i := 0; i < n; i++ {
		var x int
		fmt.Scan(&x)
		numbers = append(numbers, x)
	}
	sum := 0
	for _, x := range numbers {
		sum += x
	}
	avg := 0.0
	if n > 0 {
		// Приводим ДО деления, чтобы не потерять дробь.
		avg = float64(sum) / float64(n)
	}
	fmt.Printf("Sum: %d\n", sum)
	fmt.Printf("Avg: %.2f\n", avg)
}
@@END

@@TASK
section: 05_slices
dir: 02_min_max
num: 5_2
title: GO_05_02. Минимум и максимум
topics: срезы, `for`, `range`
input: Число N, затем N целых чисел
@@DESC
Считай `N`, затем `N` чисел и выведи минимум и максимум:

~~~text
Min: -2
Max: 9
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 5<br>3 9 -2 9 0 | Min: -2<br>Max: 9 |
| 1<br>-42 | Min: -42<br>Max: -42 |
| 4<br>-5 -1 -9 -3 | Min: -9<br>Max: -1 |
@@THEORY
## Инициализация первым элементом

~~~go
min, max := numbers[0], numbers[0]
for _, x := range numbers[1:] {
    if x < min {
        min = x
    }
    if x > max {
        max = x
    }
}
~~~

Начинать с нуля нельзя: для последовательности отрицательных чисел максимум
останется нулём.

## Срез без первого элемента

`numbers[1:]` — новый срез, который начинается со второго элемента. Исходный
срез не копируется: оба смотрят в один массив.

## Границы

~~~go
s := numbers[1:3]   // элементы с индексами 1 и 2
~~~

Правая граница не включается.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `min, max := 0, 0` | Неверно для отрицательных/положительных наборов |
| Пустой срез | Паника при `numbers[0]` |
| `x <= min` | Работает, но лишние присваивания |
@@TESTS
| `5` + `3 9 -2 9 0` | `Min: -2\nMax: 9\n` |
| `1` + `-42` | `Min: -42\nMax: -42\n` |
| `4` + `-5 -1 -9 -3` | `Min: -9\nMax: -1\n` |
| `3` + `7 7 7` | `Min: 7\nMax: 7\n` |
@@CASES
run_case $'5\n3 9 -2 9 0' $'Min: -2\nMax: 9\n'
run_case $'1\n-42' $'Min: -42\nMax: -42\n'
run_case $'4\n-5 -1 -9 -3' $'Min: -9\nMax: -1\n'
run_case $'3\n7 7 7' $'Min: 7\nMax: 7\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	numbers := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&numbers[i])
	}
	// TODO: найди минимум и максимум и выведи Min/Max
	_ = numbers
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	numbers := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&numbers[i])
	}
	min, max := numbers[0], numbers[0]
	for _, x := range numbers[1:] {
		if x < min {
			min = x
		}
		if x > max {
			max = x
		}
	}
	fmt.Printf("Min: %d\n", min)
	fmt.Printf("Max: %d\n", max)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	numbers := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&numbers[i])
	}
	// Первый элемент — корректный старт для обоих экстремумов.
	min, max := numbers[0], numbers[0]
	for _, x := range numbers[1:] {
		if x < min {
			min = x
		}
		if x > max {
			max = x
		}
	}
	fmt.Printf("Min: %d\n", min)
	fmt.Printf("Max: %d\n", max)
}
@@END

@@TASK
section: 05_slices
dir: 03_reverse_slice
num: 5_3
title: GO_05_03. Разворот среза
topics: срезы, индексы, `strings.Join`
input: Число N, затем N целых чисел
@@DESC
Считай `N`, затем `N` чисел и выведи их в обратном порядке через пробел.

Реши двумя способами: можно развернуть срез на месте, а можно просто печатать
элементы с конца.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 5<br>1 2 3 4 5 | 5 4 3 2 1 |
| 4<br>10 20 30 40 | 40 30 20 10 |
| 1<br>7 | 7 |
@@THEORY
## Разворот на месте

~~~go
for i, j := 0, len(a)-1; i < j; i, j = i+1, j-1 {
    a[i], a[j] = a[j], a[i]
}
~~~

Два индекса идут навстречу друг другу, меняя элементы местами. Когда они
встретятся, срез развёрнут.

## Вывод через Join

~~~go
parts := make([]string, len(a))
for i, x := range a {
    parts[i] = fmt.Sprint(x)
}
fmt.Println(strings.Join(parts, " "))
~~~

`fmt.Sprint` превращает значение в строку, `strings.Join` соединяет элементы
через разделитель.

## Пустой срез

Для `N = 0` `Join` вернёт пустую строку, а `Println` напечатает пустую строку.
Это ожидаемый результат.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `i <= j` | Средний элемент меняется сам с собой, не ошибка, но лишняя работа |
| Один индекс | Обрабатывается только половина |
| `Print` без разделителя | Числа склеиваются |
@@TESTS
| `5` + `1 2 3 4 5` | `5 4 3 2 1\n` |
| `4` + `10 20 30 40` | `40 30 20 10\n` |
| `1` + `7` | `7\n` |
| `0` | `\n` |
@@CASES
run_case $'5\n1 2 3 4 5' $'5 4 3 2 1\n'
run_case $'4\n10 20 30 40' $'40 30 20 10\n'
run_case $'1\n7' $'7\n'
run_case "0" $'\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	// TODO: разверни a и выведи элементы через пробел
	_ = a
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
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	for i, j := 0, len(a)-1; i < j; i, j = i+1, j-1 {
		a[i], a[j] = a[j], a[i]
	}
	parts := make([]string, len(a))
	for i, x := range a {
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
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	// Два указателя идут навстречу друг другу.
	for i, j := 0, len(a)-1; i < j; i, j = i+1, j-1 {
		a[i], a[j] = a[j], a[i]
	}
	parts := make([]string, len(a))
	for i, x := range a {
		parts[i] = fmt.Sprint(x)
	}
	fmt.Println(strings.Join(parts, " "))
}
@@END

@@TASK
section: 05_slices
dir: 04_remove_duplicates
num: 5_4
title: GO_05_04. Удаление дубликатов
topics: срезы, `map`, порядок элементов
input: Число N, затем N целых чисел
@@DESC
Удали повторяющиеся числа, сохранив порядок первого появления. Выведи результат
через пробел.

Пример: `1 2 1 3 2 4` → `1 2 3 4`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 6<br>1 2 1 3 2 4 | 1 2 3 4 |
| 4<br>3 1 3 2 | 3 1 2 |
| 5<br>5 5 5 5 5 | 5 |
@@THEORY
## Множество на map

~~~go
seen := make(map[int]bool)
unique := make([]int, 0, len(a))
for _, x := range a {
    if !seen[x] {
        seen[x] = true
        unique = append(unique, x)
    }
}
~~~

`seen[x]` возвращает `false` для отсутствующего ключа. Первое появление
запоминаем и добавляем в результат, повторы пропускаем.

## Почему порядок сохраняется

Мы обходим исходный срез по порядку и добавляем только первые вхождения,
поэтому `unique` повторяет порядок исходных данных.

## Альтернатива

Можно сразу писать в `map[int]bool` и потом сортировать ключи, но тогда
исходный порядок будет потерян.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| Сортировка ключей | Порядок отличается от исходного |
| `if seen[x]` без отрицания | Добавляются только повторы |
| `delete` вместо пропуска | Ничего не меняется |
@@TESTS
| `6` + `1 2 1 3 2 4` | `1 2 3 4\n` |
| `4` + `3 1 3 2` | `3 1 2\n` |
| `5` + `5 5 5 5 5` | `5\n` |
| `0` | `\n` |
@@CASES
run_case $'6\n1 2 1 3 2 4' $'1 2 3 4\n'
run_case $'4\n3 1 3 2' $'3 1 2\n'
run_case $'5\n5 5 5 5 5' $'5\n'
run_case "0" $'\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	// TODO: убери повторы, сохранив порядок, и выведи через пробел
	_ = a
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
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	seen := make(map[int]bool)
	unique := make([]int, 0, n)
	for _, x := range a {
		if !seen[x] {
			seen[x] = true
			unique = append(unique, x)
		}
	}
	parts := make([]string, len(unique))
	for i, x := range unique {
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
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	seen := make(map[int]bool)
	unique := make([]int, 0, n)
	for _, x := range a {
		// Первое появление запоминаем, повторы пропускаем.
		if !seen[x] {
			seen[x] = true
			unique = append(unique, x)
		}
	}
	parts := make([]string, len(unique))
	for i, x := range unique {
		parts[i] = fmt.Sprint(x)
	}
	fmt.Println(strings.Join(parts, " "))
}
@@END

@@TASK
section: 05_slices
dir: 05_sort_numbers
num: 5_5
title: GO_05_05. Сортировка чисел
topics: `sort.Ints`, срезы
input: Число N, затем N целых чисел
@@DESC
Считай `N` чисел, отсортируй их по возрастанию и выведи через пробел.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 5<br>5 1 4 2 3 | 1 2 3 4 5 |
| 4<br>-1 3 -5 0 | -5 -1 0 3 |
| 3<br>7 7 1 | 1 7 7 |
@@THEORY
## Пакет sort

~~~go
import "sort"

sort.Ints(a)
~~~

`sort.Ints` сортирует срез целых на месте, по возрастанию. Для `float64` есть
`sort.Float64s`, для строк — `sort.Strings`.

## Универсальная сортировка

~~~go
sort.Slice(a, func(i, j int) bool {
    return a[i] < a[j]
})
~~~

`sort.Slice` принимает функцию «меньше» и подходит для любых типов и
нестандартных порядков.

## Вывод

~~~go
for i, x := range a {
    if i > 0 {
        fmt.Print(" ")
    }
    fmt.Print(x)
}
fmt.Println()
~~~

Такой цикл не оставляет лишнего пробела в конце.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `sort.Ints(a)` без импорта `sort` | Ошибка компиляции |
| Сортировка копии | Исходный срез не меняется (здесь это не важно) |
| Лишний пробел в конце | Тест не пройден |
@@TESTS
| `5` + `5 1 4 2 3` | `1 2 3 4 5\n` |
| `4` + `-1 3 -5 0` | `-5 -1 0 3\n` |
| `3` + `7 7 1` | `1 7 7\n` |
| `0` | `\n` |
@@CASES
run_case $'5\n5 1 4 2 3' $'1 2 3 4 5\n'
run_case $'4\n-1 3 -5 0' $'-5 -1 0 3\n'
run_case $'3\n7 7 1' $'1 7 7\n'
run_case "0" $'\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	// TODO: отсортируй a и выведи через пробел
	_ = a
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"fmt"
	"sort"
)

func main() {
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	sort.Ints(a)
	for i, x := range a {
		if i > 0 {
			fmt.Print(" ")
		}
		fmt.Print(x)
	}
	fmt.Println()
}
@@COMMENTED
package main

import (
	"fmt"
	"sort"
)

func main() {
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	// Ints сортирует срез на месте по возрастанию.
	sort.Ints(a)
	for i, x := range a {
		if i > 0 {
			fmt.Print(" ")
		}
		fmt.Print(x)
	}
	fmt.Println()
}
@@END

@@TASK
section: 05_slices
dir: 06_rotate_slice
num: 5_6
title: GO_05_06. Циклический сдвиг
topics: срезы, `%`, индексы
input: Число N, сдвиг K, затем N целых чисел
@@DESC
Сдвинь срез **влево** на `K` позиций по кругу и выведи результат через пробел.

Пример: `1 2 3 4 5` при `K = 2` → `3 4 5 1 2`.

Если `K` больше `N`, используй остаток `K % N`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 5 2<br>1 2 3 4 5 | 3 4 5 1 2 |
| 4 0<br>1 2 3 4 | 1 2 3 4 |
| 3 4<br>7 8 9 | 8 9 7 |
@@THEORY
## Индекс со сдвигом

~~~go
shift := k % n
for i := 0; i < n; i++ {
    fmt.Print(a[(i+shift)%n], " ")
}
~~~

На позицию `i` нового среза приходит элемент, стоявший на `i + shift`.
Остаток `% n` заворачивает индекс.

## Почему остаток

Для `n = 5`, `i = 3`, `shift = 2`: `(3+2) % 5 = 0`, то есть четвёртый элемент
нового среза — первый элемент старого.

## Без лишнего пробела

~~~go
for i := 0; i < n; i++ {
    if i > 0 {
        fmt.Print(" ")
    }
    fmt.Print(a[(i+shift)%n])
}
fmt.Println()
~~~

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `k % n` при `n = 0` | Деление на ноль (паника) |
| `(i - shift + n) % n` | Сдвиг вправо |
| `a[i+shift]` без `%` | Индекс вне диапазона |
@@TESTS
| `5 2` + `1 2 3 4 5` | `3 4 5 1 2\n` |
| `4 0` + `1 2 3 4` | `1 2 3 4\n` |
| `3 4` + `7 8 9` | `8 9 7\n` |
| `1 5` + `42` | `42\n` |
| `5 7` + `1 2 3 4 5` | `3 4 5 1 2\n` |
@@CASES
run_case $'5 2\n1 2 3 4 5' $'3 4 5 1 2\n'
run_case $'4 0\n1 2 3 4' $'1 2 3 4\n'
run_case $'3 4\n7 8 9' $'8 9 7\n'
run_case $'1 5\n42' $'42\n'
run_case $'5 7\n1 2 3 4 5' $'3 4 5 1 2\n'
@@MAIN
package main

import "fmt"

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	shift := k % n
	// TODO: выведи элементы в порядке сдвига влево
	_ = shift
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	shift := k % n
	for i := 0; i < n; i++ {
		if i > 0 {
			fmt.Print(" ")
		}
		fmt.Print(a[(i+shift)%n])
	}
	fmt.Println()
}
@@COMMENTED
package main

import "fmt"

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	// Сдвиг на N возвращает срез в исходное состояние.
	shift := k % n
	for i := 0; i < n; i++ {
		if i > 0 {
			fmt.Print(" ")
		}
		// Остаток заворачивает индекс в 0..n-1.
		fmt.Print(a[(i+shift)%n])
	}
	fmt.Println()
}
@@END

@@TASK
section: 06_strings
dir: 01_string_length
num: 6_1
title: GO_06_01. Длина строки
topics: `bufio.Scanner`, `utf8.RuneCountInString`, байты и руны
input: Одна строка
@@DESC
Считай строку и выведи количество символов в ней.

Для строки `Hello` ответ `5`, для пустой строки — `0`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| Hello | 5 |
| *(пустая строка)* | 0 |
| golang | 6 |
@@THEORY
## Байты и руны

В Go строка — последовательность **байтов** в UTF-8. `len(s)` возвращает число
байтов, а не символов. Для латиницы они совпадают, для кириллицы — нет:
одна русская буква занимает 2 байта.

## Количество символов

~~~go
import "unicode/utf8"

count := utf8.RuneCountInString(s)
~~~

Руна — один символ Unicode. Для `"Привет"` `len` даст 12, а
`RuneCountInString` — 6.

## Чтение строки

~~~go
scanner := bufio.NewScanner(os.Stdin)
if scanner.Scan() {
    s := scanner.Text()
}
~~~

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `len(s)` для кириллицы | Возвращает число байтов |
| `fmt.Scan(&s)` | Читает только первое слово |
| Нет проверки `Scan()` | Пустая строка при отсутствии ввода |
@@TESTS
| `Hello` | `5\n` |
| *(пустая строка)* | `0\n` |
| `   ` | `3\n` |
| `golang` | `6\n` |
@@CASES
run_case "Hello" $'5\n'
run_case "" $'0\n'
run_case "   " $'3\n'
run_case "golang" $'6\n'
@@MAIN
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		s := scanner.Text()
		// TODO: выведи количество символов (рун) в строке
		_ = s
	}
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode/utf8"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		s := scanner.Text()
		fmt.Println(utf8.RuneCountInString(s))
	}
}
@@COMMENTED
package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode/utf8"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		s := scanner.Text()
		// len(s) — байты, RuneCountInString — символы Unicode.
		fmt.Println(utf8.RuneCountInString(s))
	}
}
@@END

@@TASK
section: 06_strings
dir: 02_count_letters_digits
num: 6_2
title: GO_06_02. Буквы и цифры
topics: `for range`, `unicode.IsLetter`, `unicode.IsDigit`
input: Одна строка
@@DESC
Посчитай количество букв и цифр в строке и выведи два числа через пробел:

~~~text
letters digits
~~~

Остальные символы (пробелы, знаки препинания) не учитываются.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| Hello123 | 5 3 |
| abc | 3 0 |
| a1b2c3 | 3 3 |
@@THEORY
## Обход рун

~~~go
for _, r := range s {
    if unicode.IsLetter(r) {
        letters++
    }
    if unicode.IsDigit(r) {
        digits++
    }
}
~~~

`range` по строке возвращает **руны**, а не байты — это важно для кириллицы.

## Проверки Unicode

| Функция | Что считает буквой/цифрой |
| --- | --- |
| `unicode.IsLetter` | любые буквы Unicode |
| `unicode.IsDigit` | десятичные цифры |
| `unicode.IsSpace` | пробелы, табы, переводы строк |

Для ASCII есть `r >= 'a' && r <= 'z'`, но Unicode-функции универсальнее.

## Вывод

~~~go
fmt.Printf("%d %d\n", letters, digits)
~~~

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `for i := 0; i < len(s); i++` | Обход байтов, кириллица ломается |
| `r >= '0' && r <= '9'` | Работает только для ASCII-цифр |
| `IsNumber` вместо `IsDigit` | Считает и римские цифры |
@@TESTS
| `Hello123` | `5 3\n` |
| `abc` | `3 0\n` |
| `12345` | `0 5\n` |
| `a1b2c3` | `3 3\n` |
| `!?.,` | `0 0\n` |
@@CASES
run_case "Hello123" $'5 3\n'
run_case "abc" $'3 0\n'
run_case "12345" $'0 5\n'
run_case "a1b2c3" $'3 3\n'
run_case "!?.," $'0 0\n'
@@MAIN
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		s := scanner.Text()
		// TODO: посчитай буквы и цифры и выведи "letters digits"
		_ = s
	}
	fmt.Println("TODO")
}
@@SOLUTION
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
		letters := 0
		digits := 0
		for _, r := range s {
			if unicode.IsLetter(r) {
				letters++
			}
			if unicode.IsDigit(r) {
				digits++
			}
		}
		fmt.Printf("%d %d\n", letters, digits)
	}
}
@@COMMENTED
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
		letters := 0
		digits := 0
		// range по строке даёт руны, а не байты.
		for _, r := range s {
			if unicode.IsLetter(r) {
				letters++
			}
			if unicode.IsDigit(r) {
				digits++
			}
		}
		fmt.Printf("%d %d\n", letters, digits)
	}
}
@@END

@@TASK
section: 06_strings
dir: 03_to_upper_lower
num: 6_3
title: GO_06_03. Верхний и нижний регистр
topics: `strings.ToUpper`, `strings.ToLower`, две строки
input: Две строки
@@DESC
Считай две строки. Первую выведи в верхнем регистре, вторую — в нижнем.

~~~text
HELLO
world
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| hello<br>WORLD | HELLO<br>world |
| Go<br>Lang | GO<br>lang |
@@THEORY
## Пакет strings

~~~go
import "strings"

upper := strings.ToUpper(first)
lower := strings.ToLower(second)
~~~

`ToUpper` и `ToLower` возвращают **новую** строку: строки в Go неизменяемы.

## Чтение двух строк

~~~go
scanner := bufio.NewScanner(os.Stdin)
scanner.Scan()
first := scanner.Text()
scanner.Scan()
second := scanner.Text()
~~~

Каждый `Scan` читает одну строку. Проверять результат нужно, если ввод может
закончиться раньше.

## Unicode

`strings.ToUpper` корректно работает с Unicode, а не только с латиницей.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `strings.ToUpper` без импорта | Ошибка компиляции |
| `fmt.Scan` для строк с пробелами | Читается только первое слово |
| Перепутаны строки | Неверный порядок вывода |
@@TESTS
| `hello` + `WORLD` | `HELLO\nworld\n` |
| `Go` + `Lang` | `GO\nlang\n` |
| *(две пустые строки)* | `\n\n` |
@@CASES
run_case $'hello\nWORLD' $'HELLO\nworld\n'
run_case $'Go\nLang' $'GO\nlang\n'
run_case $'\n' $'\n\n'
@@MAIN
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	first := scanner.Text()
	scanner.Scan()
	second := scanner.Text()
	// TODO: выведи первую строку в верхнем регистре, вторую — в нижнем
	_, _ = first, second
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	first := scanner.Text()
	scanner.Scan()
	second := scanner.Text()
	fmt.Println(strings.ToUpper(first))
	fmt.Println(strings.ToLower(second))
}
@@COMMENTED
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	first := scanner.Text()
	scanner.Scan()
	second := scanner.Text()
	// Строки неизменяемы: ToUpper/ToLower возвращают новые значения.
	fmt.Println(strings.ToUpper(first))
	fmt.Println(strings.ToLower(second))
}
@@END

@@TASK
section: 06_strings
dir: 04_count_words
num: 6_4
title: GO_06_04. Количество слов
topics: `strings.Fields`, пробельные символы
input: Одна строка
@@DESC
Посчитай количество слов в строке. Слова разделены любым количеством пробелов,
табов или переводов строк.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| hello world | 2 |
| *(пустая строка)* | 0 |
| one | 1 |
@@THEORY
## strings.Fields

~~~go
words := strings.Fields(line)
fmt.Println(len(words))
~~~

`Fields` разбивает строку по любым пробельным символам и **не создаёт пустых
элементов**. Это удобнее, чем `strings.Split(line, " ")`.

## Сравнение

| Функция | `"  a  b "` |
| --- | --- |
| `strings.Fields` | `["a", "b"]` |
| `strings.Split(s, " ")` | `["", "", "a", "", "b", ""]` |

## Пустая строка

`Fields("")` возвращает пустой срез, `len` равно `0`.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `Split` по одному пробелу | Пустые слова считаются |
| `len(line)` | Длина строки, а не число слов |
| `TrimSpace` + `Split` | Работает, но `Fields` проще |
@@TESTS
| `hello world` | `2\n` |
| *(пустая строка)* | `0\n` |
| `  a  b   c ` | `3\n` |
| `one` | `1\n` |
| `a\tb\nc` | `3\n` |
@@CASES
run_case "hello world" $'2\n'
run_case "" $'0\n'
run_case "  a  b   c " $'3\n'
run_case "one" $'1\n'
run_case $'a\tb\nc' $'3\n'
@@MAIN
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		line := scanner.Text()
		// TODO: посчитай слова и выведи их количество
		_ = line
	}
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	data, _ := io.ReadAll(os.Stdin)
	words := strings.Fields(string(data))
	fmt.Println(len(words))
}
@@COMMENTED
package main

import (
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	// Читаем весь ввод: слова могут быть разделены и переводами строк.
	data, _ := io.ReadAll(os.Stdin)
	// Fields игнорирует повторные пробелы и не даёт пустых слов.
	words := strings.Fields(string(data))
	fmt.Println(len(words))
}
@@END

@@TASK
section: 06_strings
dir: 05_reverse_string
num: 6_5
title: GO_06_05. Разворот строки
topics: руны, срезы, `strings.Builder`
input: Одна строка
@@DESC
Считай строку и выведи её в обратном порядке.

Разворачивай именно **символы**, а не байты.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| hello | olleh |
| Go | oG |
| abc def | fed cba |
@@THEORY
## Строка в руны

~~~go
runes := []rune(s)
for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
    runes[i], runes[j] = runes[j], runes[i]
}
result := string(runes)
~~~

Преобразование `[]rune(s)` разбивает строку на символы Unicode. Обратное
преобразование собирает строку.

## Почему не байты

Если развернуть `[]byte(s)`, многобайтовые символы (кириллица, эмодзи)
развалятся на части и превратятся в мусор.

## strings.Builder

Для сборки по одному символу с конца:

~~~go
var b strings.Builder
for i := len(runes) - 1; i >= 0; i-- {
    b.WriteRune(runes[i])
}
fmt.Println(b.String())
~~~

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `[]byte(s)` | Ломает Unicode |
| `for i := len(s); i > 0; i--` | Индексы байтов, а не рун |
| Пустая строка | Должна дать пустой вывод, без паники |
@@TESTS
| `hello` | `olleh\n` |
| `Go` | `oG\n` |
| *(пустая строка)* | `\n` |
| `abc def` | `fed cba\n` |
@@CASES
run_case "hello" $'olleh\n'
run_case "Go" $'oG\n'
run_case "" $'\n'
run_case "abc def" $'fed cba\n'
@@MAIN
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		s := scanner.Text()
		// TODO: разверни строку по символам и выведи результат
		_ = s
	}
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		s := scanner.Text()
		runes := []rune(s)
		for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
			runes[i], runes[j] = runes[j], runes[i]
		}
		fmt.Println(string(runes))
	}
}
@@COMMENTED
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		s := scanner.Text()
		// []rune разбивает строку на символы Unicode, а не байты.
		runes := []rune(s)
		for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
			runes[i], runes[j] = runes[j], runes[i]
		}
		fmt.Println(string(runes))
	}
}
@@END

@@TASK
section: 06_strings
dir: 06_palindrome
num: 6_6
title: GO_06_06. Палиндром
topics: `unicode`, нормализация строки
input: Одна строка
@@DESC
Определи, является ли строка палиндромом. Учитывай только буквы и цифры,
игнорируя регистр, пробелы и знаки препинания.

Выведи `true` или `false`.

Пример: `A man, a plan, a canal: Panama` → `true`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| A man, a plan, a canal: Panama | true |
| hello | false |
| 12321 | true |
@@THEORY
## Нормализация

Собери новую последовательность только из букв и цифр, приведённых к нижнему
регистру:

~~~go
var normalized []rune
for _, r := range s {
    if unicode.IsLetter(r) || unicode.IsDigit(r) {
        normalized = append(normalized, unicode.ToLower(r))
    }
}
~~~

## Проверка

~~~go
ok := true
for i, j := 0, len(normalized)-1; i < j; i, j = i+1, j-1 {
    if normalized[i] != normalized[j] {
        ok = false
        break
    }
}
fmt.Println(ok)
~~~

## Пустая строка

Пустая строка (и строка только из знаков препинания) считается палиндромом:
сравнивать нечего, условие не нарушено.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| Сравнение без `ToLower` | `Aa` не считается палиндромом |
| Учёт пробелов | `a b a` ошибочно не палиндром |
| Разворот байтов | Ломает Unicode |
@@TESTS
| `A man, a plan, a canal: Panama` | `true\n` |
| `hello` | `false\n` |
| `12321` | `true\n` |
| *(пустая строка)* | `true\n` |
| `No lemon, no melon` | `true\n` |
| `abc` | `false\n` |
@@CASES
run_case "A man, a plan, a canal: Panama" $'true\n'
run_case "hello" $'false\n'
run_case "12321" $'true\n'
run_case "" $'true\n'
run_case "No lemon, no melon" $'true\n'
run_case "abc" $'false\n'
@@MAIN
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		s := scanner.Text()
		// TODO: проверь палиндром и выведи true/false
		_ = s
	}
	fmt.Println("TODO")
}
@@SOLUTION
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
@@COMMENTED
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
		// Оставляем только буквы и цифры в нижнем регистре.
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
@@END

@@TASK
section: 06_strings
dir: 07_caesar_cipher
num: 6_7
title: GO_06_07. Шифр Цезаря
topics: руны, арифметика символов, `bufio.Scanner`
input: Сдвиг K и строка
@@DESC
Считай сдвиг `K` и строку. Зашифруй строку шифром Цезаря: каждая латинская
буква сдвигается на `K` позиций по кругу, регистр сохраняется. Остальные
символы не меняются.

~~~text
3
Hello, World!
~~~

→

~~~text
Khoor, Zruog!
~~~

Сдвиг может быть отрицательным или больше 26.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 3<br>Hello, World! | Khoor, Zruog! |
| 1<br>abcXYZ | bcdYZA |
| 0<br>No change | No change |
@@THEORY
## Чтение двух строк

`fmt.Scan` для числа оставляет `\n` в потоке. Надёжнее читать обе строки
через `bufio.Scanner`:

~~~go
scanner := bufio.NewScanner(os.Stdin)
scanner.Scan()
var shift int
fmt.Sscanf(scanner.Text(), "%d", &shift)
scanner.Scan()
line := scanner.Text()
~~~

## Нормализация сдвига

~~~go
shift = ((shift % 26) + 26) % 26
~~~

Так `-1` превращается в `25`, а `29` — в `3`.

## Сдвиг буквы

~~~go
if r >= 'a' && r <= 'z' {
    r = 'a' + (r-'a'+rune(shift))%26
}
~~~

Для заглавных — аналогично с `'A'`.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| Нет нормализации | Отрицательный сдвиг даёт странные символы |
| Сдвиг без `% 26` | Выход за пределы алфавита |
| `fmt.Scan` + `nextLine` | Пустая строка из-за оставшегося `\n` |
@@TESTS
| `3` + `Hello, World!` | `Khoor, Zruog!\n` |
| `1` + `abcXYZ` | `bcdYZA\n` |
| `0` + `No change` | `No change\n` |
| `26` + `abc` | `abc\n` |
| `-1` + `abc` | `zab\n` |
@@CASES
run_case $'3\nHello, World!' $'Khoor, Zruog!\n'
run_case $'1\nabcXYZ' $'bcdYZA\n'
run_case $'0\nNo change' $'No change\n'
run_case $'26\nabc' $'abc\n'
run_case $'-1\nabc' $'zab\n'
@@MAIN
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
	// TODO: зашифруй line сдвигом shift и выведи результат
	_ = line
	fmt.Println("TODO")
}
@@SOLUTION
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
@@COMMENTED
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

	// Приводим сдвиг к диапазону 0..25, чтобы работали -1 и 29.
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
@@END
