@@TASK
section: 03_expressions
dir: 01_circle_area
num: 3_1
title: GO_03_01. Площадь круга
topics: `float64`, `math.Pi`, `fmt.Printf`
input: Радиус круга (вещественное число)
@@DESC
Считай радиус круга и выведи площадь с двумя знаками после точки:

~~~text
Area: 3.14
~~~

Формула: `π · r²`. Используй `math.Pi`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 1 | Area: 3.14 |
| 2 | Area: 12.57 |
| 0 | Area: 0.00 |
@@THEORY
## Константа π

~~~go
import "math"

area := math.Pi * r * r
~~~

`math.Pi` — константа типа `float64` с достаточной точностью.

## Возведение в квадрат

В Go нет оператора `**`. Квадрат записывают как `r * r` или используют
`math.Pow(r, 2)`, но умножение быстрее и проще.

## Форматирование

~~~go
fmt.Printf("Area: %.2f\n", area)
~~~

## Проверка типов

`fmt.Scan(&r)` для `var r float64` читает и `2`, и `2.5`. Если объявить `r` как
`int`, ввод `2.5` не будет прочитан.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `math.Pi * r * 2` | Это длина окружности, а не площадь |
| `r ^ 2` | `^` — побитовое XOR, не степень |
| `%d` для площади | Неверный формат |
@@TESTS
| `1` | `Area: 3.14\n` |
| `2` | `Area: 12.57\n` |
| `0` | `Area: 0.00\n` |
| `2.5` | `Area: 19.63\n` |
@@CASES
run_case "1" $'Area: 3.14\n'
run_case "2" $'Area: 12.57\n'
run_case "0" $'Area: 0.00\n'
run_case "2.5" $'Area: 19.63\n'
@@MAIN
package main

import (
	"fmt"
	"math"
)

func main() {
	var r float64
	fmt.Scan(&r)
	// TODO: посчитай площадь math.Pi * r * r и выведи Area: <число>
	_ = math.Pi
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"fmt"
	"math"
)

func main() {
	var r float64
	fmt.Scan(&r)
	area := math.Pi * r * r
	fmt.Printf("Area: %.2f\n", area)
}
@@COMMENTED
package main

import (
	"fmt"
	"math"
)

func main() {
	var r float64
	fmt.Scan(&r)
	// Площадь круга: π * r^2. В Go степень через умножение.
	area := math.Pi * r * r
	fmt.Printf("Area: %.2f\n", area)
}
@@END

@@TASK
section: 03_expressions
dir: 02_radians_to_degrees
num: 3_2
title: GO_03_02. Радианы в градусы
topics: `float64`, `math.Pi`, преобразование единиц
input: Угол в радианах
@@DESC
Считай угол в радианах и переведи его в градусы:

~~~text
Degrees: 180.00
~~~

Формула: `градусы = радианы · 180 / π`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 3.141592653589793 | Degrees: 180.00 |
| 1.5707963267948966 | Degrees: 90.00 |
| 0 | Degrees: 0.00 |
@@THEORY
## Преобразование

~~~go
degrees := radians * 180 / math.Pi
~~~

Порядок операций: умножение и деление выполняются слева направо, поэтому
`radians * 180 / math.Pi` даёт правильный результат.

## Вещественная арифметика

Все операнды должны быть `float64`. Если написать `180`, константа всё равно
преобразуется к `float64`, потому что `radians` уже `float64`.

## Округление при выводе

`%.2f` округляет, а не обрезает. Например, `57.295779...` станет `57.30`.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `radians * math.Pi / 180` | Обратное преобразование |
| `180 / math.Pi * radians` | Ошибка порядка не будет, но читается хуже |
| `%.0f` | Потеря дробной части |
@@TESTS
| `3.141592653589793` | `Degrees: 180.00\n` |
| `1.5707963267948966` | `Degrees: 90.00\n` |
| `0` | `Degrees: 0.00\n` |
| `1` | `Degrees: 57.30\n` |
@@CASES
run_case "3.141592653589793" $'Degrees: 180.00\n'
run_case "1.5707963267948966" $'Degrees: 90.00\n'
run_case "0" $'Degrees: 0.00\n'
run_case "1" $'Degrees: 57.30\n'
@@MAIN
package main

import (
	"fmt"
	"math"
)

func main() {
	var radians float64
	fmt.Scan(&radians)
	// TODO: переведи радианы в градусы и выведи Degrees: <число>
	_ = math.Pi
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"fmt"
	"math"
)

func main() {
	var radians float64
	fmt.Scan(&radians)
	degrees := radians * 180 / math.Pi
	fmt.Printf("Degrees: %.2f\n", degrees)
}
@@COMMENTED
package main

import (
	"fmt"
	"math"
)

func main() {
	var radians float64
	fmt.Scan(&radians)
	// 180 градусов соответствуют π радианам.
	degrees := radians * 180 / math.Pi
	fmt.Printf("Degrees: %.2f\n", degrees)
}
@@END

@@TASK
section: 03_expressions
dir: 03_swap_edge_digits
num: 3_3
title: GO_03_03. Перестановка крайних цифр
topics: `%`, `/`, цикл для поиска разряда
input: Целое число, не меньшее 10
@@DESC
Поменяй местами первую и последнюю цифры числа и выведи результат.

Пример: `1234` → `4231`.

Если после перестановки в начале оказывается ноль, он не печатается:
`10` → `1`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 1234 | 4231 |
| 12345 | 52341 |
| 10 | 1 |
@@THEORY
## Разряды

Чтобы поменять крайние цифры, нужно знать старший разряд:

~~~go
divisor := 1
for n/divisor >= 10 {
    divisor *= 10
}
~~~

Для `1234` цикл даст `divisor = 1000`.

## Крайние цифры

~~~go
first := n / divisor
last := n % 10
middle := (n % divisor) / 10
~~~

`middle` — всё, что между первой и последней цифрой.

## Сборка числа

~~~go
result := last*divisor + middle*10 + first
~~~

Для `1234`: `4*1000 + 23*10 + 1 = 4231`.

## Ноль в начале

Для `10`: `last = 0`, `result = 0*10 + 0 + 1 = 1`. Ведущий ноль не хранится в
числе, поэтому вывод — `1`.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `divisor` начинается с 0 | Деление на ноль |
| `middle := n % divisor` | В `middle` попадает последняя цифра |
| Забыть про `n < 10` | Неверный разряд |
@@TESTS
| `1234` | `4231\n` |
| `12345` | `52341\n` |
| `10` | `1\n` |
| `99` | `99\n` |
| `102` | `201\n` |
@@CASES
run_case "1234" $'4231\n'
run_case "12345" $'52341\n'
run_case "10" $'1\n'
run_case "99" $'99\n'
run_case "102" $'201\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	divisor := 1
	for n/divisor >= 10 {
		divisor *= 10
	}
	// TODO: поменяй первую и последнюю цифры и выведи результат
	_ = divisor
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	divisor := 1
	for n/divisor >= 10 {
		divisor *= 10
	}
	first := n / divisor
	last := n % 10
	middle := (n % divisor) / 10
	result := last*divisor + middle*10 + first
	fmt.Println(result)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// divisor — степень десяти, соответствующая старшей цифре.
	divisor := 1
	for n/divisor >= 10 {
		divisor *= 10
	}
	first := n / divisor
	last := n % 10
	middle := (n % divisor) / 10
	// Собираем число: последняя цифра, середина, первая цифра.
	result := last*divisor + middle*10 + first
	fmt.Println(result)
}
@@END

@@TASK
section: 03_expressions
dir: 04_integer_division_trap
num: 3_4
title: GO_03_04. Ловушка целочисленного деления
topics: целочисленное деление, приведение типов, `float64`
input: Два целых числа
@@DESC
Считай два целых числа `a` и `b` и выведи их среднее арифметическое с двумя
знаками после точки.

~~~text
Avg: 3.50
~~~

Обрати внимание: `(a + b) / 2` при целых `a` и `b` даст целое число и потеряет
дробную часть.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 3 4 | Avg: 3.50 |
| 1 2 | Avg: 1.50 |
| -3 4 | Avg: 0.50 |
@@THEORY
## Целочисленное деление

~~~go
average := (a + b) / 2
~~~

Если `a = 3`, `b = 4`, сумма 7, а `7 / 2` равно `3`, а не `3.5`. Дробная часть
отбрасывается.

## Приведение к float64

~~~go
average := float64(a+b) / 2.0
~~~

Сначала сумма преобразуется в `float64`, затем деление становится
вещественным.

## Альтернатива

~~~go
average := float64(a+b) / float64(2)
~~~

`2.0` — нетипизированная константа, она автоматически станет `float64`.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `float64(a+b/2)` | Сначала целое деление, потом приведение |
| `(a + b) / 2.0` с int-переменными | Ошибка компиляции: нельзя `int / float64` |
| `%.0f` | Дробная часть не печатается |
@@TESTS
| `3 4` | `Avg: 3.50\n` |
| `1 2` | `Avg: 1.50\n` |
| `-3 4` | `Avg: 0.50\n` |
| `5 5` | `Avg: 5.00\n` |
@@CASES
run_case "3 4" $'Avg: 3.50\n'
run_case "1 2" $'Avg: 1.50\n'
run_case "-3 4" $'Avg: 0.50\n'
run_case "5 5" $'Avg: 5.00\n'
run_case $'2\n3' $'Avg: 2.50\n'
@@MAIN
package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	// TODO: посчитай среднее как float64 и выведи Avg: <число>
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	average := float64(a+b) / 2.0
	fmt.Printf("Avg: %.2f\n", average)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	// Приводим сумму к float64 ДО деления, иначе дробь потеряется.
	average := float64(a+b) / 2.0
	fmt.Printf("Avg: %.2f\n", average)
}
@@END

@@TASK
section: 03_expressions
dir: 05_boolean_expression
num: 3_5
title: GO_03_05. Логическое выражение
topics: `%`, `||`, `bool`
input: Одно целое число
@@DESC
Выведи `true`, если число делится на 3 **или** заканчивается на 7.
Иначе выведи `false`.

Примеры: `9` → `true`, `17` → `true`, `10` → `false`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 9 | true |
| 17 | true |
| 10 | false |
@@THEORY
## Условие

~~~go
result := n%3 == 0 || n%10 == 7
fmt.Println(result)
~~~

- `n%3 == 0` проверяет делимость на 3;
- `n%10 == 7` проверяет последнюю цифру;
- `||` — логическое «или» (хотя бы одно условие истинно).

## Логические операторы

| Оператор | Смысл |
| --- | --- |
| `&&` | и |
| `\|\|` | или |
| `!` | не |

`||` и `&&` вычисляются с сокращением: если результат уже ясен, правая часть
не вычисляется.

## Отрицательные числа

В Go остаток сохраняет знак делимого: `-9 % 3 == 0`, `-17 % 10 == -7`.
Для проверки последней цифры отрицательного числа удобнее `n%10 == 7 || n%10 == -7`
или работать с модулем.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `n/3 == 0` | Проверка «меньше 3», а не делимости |
| `n%10 = 7` | Присваивание вместо сравнения |
| `and`/`or` | В Go нет таких ключевых слов |
@@TESTS
| `9` | `true\n` |
| `17` | `true\n` |
| `10` | `false\n` |
| `21` | `true\n` |
| `0` | `true\n` |
| `7` | `true\n` |
@@CASES
run_case "9" $'true\n'
run_case "17" $'true\n'
run_case "10" $'false\n'
run_case "21" $'true\n'
run_case "0" $'true\n'
run_case "7" $'true\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// TODO: проверь n%3 == 0 или n%10 == 7 и выведи true/false
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	result := n%3 == 0 || n%10 == 7
	fmt.Println(result)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// Делится на 3 ИЛИ оканчивается на 7.
	result := n%3 == 0 || n%10 == 7
	fmt.Println(result)
}
@@END

@@TASK
section: 04_loops
dir: 01_sequence_max
num: 4_1
title: GO_04_01. Максимум последовательности
topics: `for`, чтение последовательности
input: Число N, затем N целых чисел
@@DESC
Считай `N`, затем `N` целых чисел. Выведи максимальное из них.

Гарантируется, что `N >= 1`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 5<br>3 9 -2 9 0 | 9 |
| 1<br>-42 | -42 |
| 4<br>-5 -1 -9 -3 | -1 |
@@THEORY
## Чтение N чисел

~~~go
var n int
fmt.Scan(&n)

var max int
fmt.Scan(&max)

for i := 1; i < n; i++ {
    var x int
    fmt.Scan(&x)
    if x > max {
        max = x
    }
}
~~~

Первый элемент становится начальным максимумом. Инициализация нулём неверна:
если все числа отрицательные, максимум останется нулём.

## Цикл for

В Go есть только `for`, но он покрывает все формы:

~~~go
for i := 0; i < n; i++ { }   // классический
for condition { }            // while
for { }                      // бесконечный
for i, v := range slice { }  // обход коллекции
~~~

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `max := 0` | Для отрицательных чисел ответ 0 |
| Цикл до `i <= n` | Лишнее чтение, зависание на EOF |
| `min` вместо `max` | Неверный ответ |
@@TESTS
| `5` + `3 9 -2 9 0` | `9\n` |
| `1` + `-42` | `-42\n` |
| `4` + `-5 -1 -9 -3` | `-1\n` |
| `3` + `7 7 7` | `7\n` |
@@CASES
run_case $'5\n3 9 -2 9 0' $'9\n'
run_case $'1\n-42' $'-42\n'
run_case $'4\n-5 -1 -9 -3' $'-1\n'
run_case $'3\n7 7 7' $'7\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	var max int
	fmt.Scan(&max)
	for i := 1; i < n; i++ {
		var x int
		fmt.Scan(&x)
		// TODO: обнови max, если x больше
		_ = x
	}
	fmt.Println(max)
}
@@SOLUTION
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	var max int
	fmt.Scan(&max)
	for i := 1; i < n; i++ {
		var x int
		fmt.Scan(&x)
		if x > max {
			max = x
		}
	}
	fmt.Println(max)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// Первый элемент — начальный максимум.
	var max int
	fmt.Scan(&max)
	for i := 1; i < n; i++ {
		var x int
		fmt.Scan(&x)
		if x > max {
			max = x
		}
	}
	fmt.Println(max)
}
@@END

@@TASK
section: 04_loops
dir: 02_sum_of_digits
num: 4_2
title: GO_04_02. Сумма цифр
topics: `%`, `/`, `for`
input: Одно целое число
@@DESC
Считай целое число и выведи сумму его цифр.

Для отрицательного числа цифры берутся по модулю: `-123` → `1 + 2 + 3 = 6`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 12345 | 15 |
| 0 | 0 |
| -123 | 6 |
@@THEORY
## Разбор цифр

~~~go
sum := 0
for n > 0 {
    sum += n % 10
    n /= 10
}
~~~

`n % 10` даёт последнюю цифру, `n / 10` отбрасывает её. Цикл продолжается, пока
число не станет нулём.

## Отрицательные числа

Остаток в Go сохраняет знак: `-123 % 10 == -3`. Поэтому сначала берём модуль:

~~~go
if n < 0 {
    n = -n
}
~~~

## Ноль

Для `n = 0` цикл не выполнится, сумма останется `0` — это правильный ответ.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `for n >= 0` | Бесконечный цикл |
| Нет `n /= 10` | Бесконечный цикл |
| Не обработан минус | Сумма отрицательная |
@@TESTS
| `12345` | `15\n` |
| `0` | `0\n` |
| `9999` | `36\n` |
| `7` | `7\n` |
| `1000` | `1\n` |
| `2000000000` | `2\n` |
@@CASES
run_case "12345" $'15\n'
run_case "0" $'0\n'
run_case "9999" $'36\n'
run_case "7" $'7\n'
run_case "1000" $'1\n'
run_case "2000000000" $'2\n'
run_case "-123" $'6\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// TODO: посчитай сумму цифр и выведи её
	_ = n
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	if n < 0 {
		n = -n
	}
	sum := 0
	for n > 0 {
		sum += n % 10
		n /= 10
	}
	fmt.Println(sum)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// Для отрицательных чисел работаем с модулем.
	if n < 0 {
		n = -n
	}
	sum := 0
	for n > 0 {
		sum += n % 10 // последняя цифра
		n /= 10       // отбрасываем её
	}
	fmt.Println(sum)
}
@@END

@@TASK
section: 04_loops
dir: 03_max_digit
num: 4_3
title: GO_04_03. Максимальная цифра
topics: `%`, `/`, `for`
input: Одно целое число
@@DESC
Считай целое число и выведи его максимальную цифру.

Для отрицательного числа знак игнорируется: `-907` → `9`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 2739 | 9 |
| 0 | 0 |
| 907 | 9 |
@@THEORY
## Поиск максимума среди цифр

~~~go
max := 0
for n > 0 {
    digit := n % 10
    if digit > max {
        max = digit
    }
    n /= 10
}
~~~

Начальное значение `0` корректно, потому что цифры неотрицательны.

## Отрицательный ввод

~~~go
if n < 0 {
    n = -n
}
~~~

## Ноль

Для `0` цикл не выполнится, останется `0`. Это и есть максимальная цифра.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `max := 9` | Для числа без девяток ответ неверный |
| `if digit < max` | Ищется минимум |
| Нет деления на 10 | Бесконечный цикл |
@@TESTS
| `2739` | `9\n` |
| `0` | `0\n` |
| `1111` | `1\n` |
| `907` | `9\n` |
| `1234567890` | `9\n` |
| `-907` | `9\n` |
@@CASES
run_case "2739" $'9\n'
run_case "0" $'0\n'
run_case "1111" $'1\n'
run_case "907" $'9\n'
run_case "1234567890" $'9\n'
run_case "-907" $'9\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	if n < 0 {
		n = -n
	}
	// TODO: найди максимальную цифру и выведи её
	_ = n
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	if n < 0 {
		n = -n
	}
	max := 0
	for n > 0 {
		digit := n % 10
		if digit > max {
			max = digit
		}
		n /= 10
	}
	fmt.Println(max)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	if n < 0 {
		n = -n
	}
	// Цифры лежат в диапазоне 0..9, поэтому 0 — корректный старт.
	max := 0
	for n > 0 {
		digit := n % 10
		if digit > max {
			max = digit
		}
		n /= 10
	}
	fmt.Println(max)
}
@@END

@@TASK
section: 04_loops
dir: 04_reverse_number
num: 4_4
title: GO_04_04. Разворот числа
topics: `%`, `/`, накопление результата
input: Одно целое число
@@DESC
Считай целое число и выведи его цифры в обратном порядке, как число.

Примеры: `12340` → `4321`, `100` → `1`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 12340 | 4321 |
| 0 | 0 |
| 100 | 1 |
@@THEORY
## Накопление разрядов

~~~go
reversed := 0
for n > 0 {
    reversed = reversed*10 + n%10
    n /= 10
}
~~~

На каждом шаге к результату добавляется новая цифра справа.

Пример для `123`:

| Шаг | n | digit | reversed |
| --- | --- | --- | --- |
| 1 | 123 | 3 | 3 |
| 2 | 12 | 2 | 32 |
| 3 | 1 | 1 | 321 |

## Ведущие нули

Для `100`: `reversed` станет `1` — ведущие нули в числе не хранятся. Для
`12340` результат `4321`, а не `04321`.

## Отрицательные числа

Обрабатывай модуль и выводи знак отдельно, если это нужно. В этом задании
достаточно модуля: `-123` → `321`.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `reversed += n % 10` | Цифры складываются, а не сдвигаются |
| Забыт `*10` | Сумма цифр вместо разворота |
| Нет `n /= 10` | Бесконечный цикл |
@@TESTS
| `12340` | `4321\n` |
| `0` | `0\n` |
| `100` | `1\n` |
| `7` | `7\n` |
| `1234567899` | `9987654321\n` |
| `-123` | `321\n` |
@@CASES
run_case "12340" $'4321\n'
run_case "0" $'0\n'
run_case "100" $'1\n'
run_case "7" $'7\n'
run_case "1234567899" $'9987654321\n'
run_case "-123" $'321\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	if n < 0 {
		n = -n
	}
	// TODO: разверни число и выведи результат
	_ = n
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	if n < 0 {
		n = -n
	}
	reversed := 0
	for n > 0 {
		reversed = reversed*10 + n%10
		n /= 10
	}
	fmt.Println(reversed)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	if n < 0 {
		n = -n
	}
	reversed := 0
	for n > 0 {
		// Сдвигаем уже собранные цифры влево и добавляем новую справа.
		reversed = reversed*10 + n%10
		n /= 10
	}
	fmt.Println(reversed)
}
@@END

@@TASK
section: 04_loops
dir: 05_fizzbuzz
num: 4_5
title: GO_04_05. FizzBuzz
topics: `for`, `%`, `if`/`else if`
input: Одно целое число N
@@DESC
Выведи числа от 1 до `N` по одному в строке, но:

- вместо чисел, кратных 3, — `Fizz`;
- вместо чисел, кратных 5, — `Buzz`;
- вместо чисел, кратных и 3, и 5, — `FizzBuzz`.

Пример для `N = 5`:

~~~text
1
2
Fizz
4
Buzz
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 5 | 1<br>2<br>Fizz<br>4<br>Buzz |
| 3 | 1<br>2<br>Fizz |
| 0 | *(пусто)* |
@@THEORY
## Порядок проверок

Сначала проверяй кратность 15 (3 и 5), потом 3, потом 5:

~~~go
for i := 1; i <= n; i++ {
    switch {
    case i%15 == 0:
        fmt.Println("FizzBuzz")
    case i%3 == 0:
        fmt.Println("Fizz")
    case i%5 == 0:
        fmt.Println("Buzz")
    default:
        fmt.Println(i)
    }
}
~~~

Если проверить `i%3` раньше, число 15 напечатает `Fizz`, а не `FizzBuzz`.

## switch без выражения

`switch { case condition: }` заменяет цепочку `if/else if`. Ветки проверяются
сверху вниз, срабатывает первая истинная.

## Пустой диапазон

При `N = 0` цикл не выполнится ни разу, вывод будет пустым. Это корректно.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `i%3` раньше `i%15` | Для 15 выводится `Fizz` |
| `i < n` вместо `i <= n` | Не печатается последнее число |
| `Print` вместо `Println` | Все ответы на одной строке |
@@TESTS
| `5` | `1\n2\nFizz\n4\nBuzz\n` |
| `3` | `1\n2\nFizz\n` |
| `0` | *(пусто)* |
| `15` | `1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n` |
@@CASES
run_case "5" $'1\n2\nFizz\n4\nBuzz\n'
run_case "3" $'1\n2\nFizz\n'
run_case_devnull ""
run_case "0" ""
run_case "15" $'1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	for i := 1; i <= n; i++ {
		// TODO: выведи FizzBuzz, Fizz, Buzz или число
		_ = i
	}
}
@@SOLUTION
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	for i := 1; i <= n; i++ {
		switch {
		case i%15 == 0:
			fmt.Println("FizzBuzz")
		case i%3 == 0:
			fmt.Println("Fizz")
		case i%5 == 0:
			fmt.Println("Buzz")
		default:
			fmt.Println(i)
		}
	}
}
@@COMMENTED
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	for i := 1; i <= n; i++ {
		// Кратность 15 проверяем первой, иначе 15 станет Fizz.
		switch {
		case i%15 == 0:
			fmt.Println("FizzBuzz")
		case i%3 == 0:
			fmt.Println("Fizz")
		case i%5 == 0:
			fmt.Println("Buzz")
		default:
			fmt.Println(i)
		}
	}
}
@@END

@@TASK
section: 04_loops
dir: 06_unpaired_number
num: 4_6
title: GO_04_06. Число без пары
topics: XOR `^`, `for`
input: Число N, затем N целых чисел
@@DESC
В последовательности каждое число встречается дважды, кроме одного. Найди и
выведи число без пары.

Реши за один проход и без дополнительных коллекций — через XOR.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 5<br>1 2 3 2 1 | 3 |
| 3<br>4 4 -7 | -7 |
| 1<br>42 | 42 |
@@THEORY
## Свойства XOR

Побитовое исключающее ИЛИ (`^`) обладает нужными свойствами:

- `x ^ x == 0` — одинаковые числа взаимно уничтожаются;
- `x ^ 0 == x`;
- операция коммутативна и ассоциативна.

Если сложить XOR всех чисел, пары исчезнут, и останется единственное число без
пары.

## Код

~~~go
result := 0
for i := 0; i < n; i++ {
    var x int
    fmt.Scan(&x)
    result ^= x
}
fmt.Println(result)
~~~

## Почему это работает

Порядок не важен: `1 ^ 2 ^ 3 ^ 2 ^ 1` можно переставить в
`(1 ^ 1) ^ (2 ^ 2) ^ 3 = 0 ^ 0 ^ 3 = 3`.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `result += x` | Сумма, а не XOR |
| `result \|= x` | Побитовое ИЛИ не уничтожает пары |
| Чтение N+1 числа | Лишний ввод или зависание |
@@TESTS
| `5` + `1 2 3 2 1` | `3\n` |
| `3` + `4 4 -7` | `-7\n` |
| `1` + `42` | `42\n` |
| `5` + `8 8 0 0 5` | `5\n` |
@@CASES
run_case $'5\n1 2 3 2 1' $'3\n'
run_case $'3\n4 4 -7' $'-7\n'
run_case $'1\n42' $'42\n'
run_case $'5\n8 8 0 0 5' $'5\n'
run_case $'7\n1 2 3 1 3 2 9' $'9\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	result := 0
	for i := 0; i < n; i++ {
		var x int
		fmt.Scan(&x)
		// TODO: добавь x в result через XOR
		_ = x
	}
	fmt.Println(result)
}
@@SOLUTION
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	result := 0
	for i := 0; i < n; i++ {
		var x int
		fmt.Scan(&x)
		result ^= x
	}
	fmt.Println(result)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	result := 0
	for i := 0; i < n; i++ {
		var x int
		fmt.Scan(&x)
		// Пары одинаковых чисел дают 0, остаётся число без пары.
		result ^= x
	}
	fmt.Println(result)
}
@@END
