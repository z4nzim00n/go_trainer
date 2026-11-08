@@TASK
section: 01_basics
dir: 01_hello_world
num: 1_1
title: GO_01_01. Первая программа
topics: `package main`, `func main`, `fmt.Println`
input: Не требуются
@@DESC
Напиши программу, которая выводит строку:

~~~text
Hello, Go!
~~~

Каждая программа на Go начинается с объявления пакета. Исполняемая программа
обязательно находится в `package main` и содержит функцию `main`.

~~~go
package main

import "fmt"

func main() {
    fmt.Println("Hello, Go!")
}
~~~

`fmt.Println` печатает значение и добавляет перевод строки.
@@EXAMPLES
| *(нет ввода)* | `Hello, Go!` |
@@THEORY
## Пакет

Любой файл Go начинается с объявления пакета:

~~~go
package main
~~~

Для исполняемой программы имя пакета должно быть `main`. Если назвать его
иначе, компилятор создаст библиотечный пакет, и запустить его напрямую нельзя.

## Точка входа

~~~go
func main() {
}
~~~

`main` — функция без параметров и без возвращаемого значения. С неё начинается
выполнение программы.

## Вывод

~~~go
import "fmt"

fmt.Println("Hello, Go!")
~~~

`fmt` — пакет форматированного ввода-вывода из стандартной библиотеки.
`Println` печатает аргументы через пробел и добавляет `\n`.

| Функция | Перевод строки | Пример |
| --- | --- | --- |
| `fmt.Print` | нет | `fmt.Print("a"); fmt.Print("b")` → `ab` |
| `fmt.Println` | да | `fmt.Println("a")` → `a\n` |
| `fmt.Printf` | зависит от формата | `fmt.Printf("%s\n", "a")` |

## Частые ошибки

| Ошибка | Сообщение компилятора |
| --- | --- |
| `package mian` | программа не является `package main` |
| Нет `func main` | `function main is undeclared in the main package` |
| Нет `import "fmt"` | `undefined: fmt` |
| Лишний импорт | `"fmt" imported and not used` |
@@TESTS
| *(нет ввода)* | `Hello, Go!\n` |
@@CASES
run_case_devnull $'Hello, Go!\n'
@@MAIN
package main

import "fmt"

func main() {
	// TODO: выведи строку Hello, Go! с переносом строки в конце
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	fmt.Println("Hello, Go!")
}
@@COMMENTED
package main

import "fmt"

func main() {
	// Println печатает строку и добавляет перевод строки.
	fmt.Println("Hello, Go!")
}
@@END

@@TASK
section: 01_basics
dir: 02_fix_package_name
num: 1_2
title: GO_01_02. Исправь имя пакета
topics: `package main`, ошибки компиляции
input: Не требуются
@@DESC
В файле `main.go` есть ошибка: пакет объявлен как `mian`. Из-за этого программа
не собирается как исполняемая.

Исправь объявление пакета так, чтобы программа запускалась и выводила:

~~~text
Fixed!
~~~

Подсказка: для запуска нужен пакет `main`.

Это задание «найди и исправь ошибку»: стартовый файл намеренно **не
компилируется**.
@@EXAMPLES
| *(нет ввода)* | `Fixed!` |
@@THEORY
## Имя пакета

Первая строка каждого файла Go:

~~~go
package имя
~~~

Для исполняемой программы имя ровно одно — `main`. Регистр важен: `Main`,
`MAIN` и `mian` — разные имена, и ни одно из них не даст исполняемую программу.

## Как Go находит точку входа

Компилятор собирает пакет `main` и ищет в нём `func main()`. Если пакет назван
не `main`, получается библиотека: её можно импортировать, но нельзя запустить
командой `go run`.

## Как читать ошибку

~~~text
package mian is not a main package
~~~

Сообщение прямо указывает: пакет не является `main`. Исправление — поменять
одно слово в первой строке.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `package Main` | Регистр не тот, пакет не `main` |
| Опечатка `mian` | Не исполняемый пакет |
| Убрать строку `package` | Синтаксическая ошибка в первой строке |
@@TESTS
| *(нет ввода)* | `Fixed!\n` |
@@CASES
run_case_devnull $'Fixed!\n'
@@MAIN
package mian

import "fmt"

func main() {
	fmt.Println("Fixed!")
}
@@SOLUTION
package main

import "fmt"

func main() {
	fmt.Println("Fixed!")
}
@@COMMENTED
package main

import "fmt"

func main() {
	// Пакет main делает программу исполняемой.
	fmt.Println("Fixed!")
}
@@END

@@TASK
section: 01_basics
dir: 03_fix_missing_import
num: 1_3
title: GO_01_03. Исправь отсутствующий импорт
topics: `import`, `fmt`, ошибки компиляции
input: Не требуются
@@DESC
Программа использует `fmt.Println`, но забыла импортировать пакет `fmt`,
поэтому не компилируется.

Добавь нужный импорт, чтобы программа вывела:

~~~text
Imported!
~~~

Это задание «найди и исправь ошибку»: стартовый файл намеренно **не
компилируется**.
@@EXAMPLES
| *(нет ввода)* | `Imported!` |
@@THEORY
## Импорт пакета

~~~go
import "fmt"
~~~

Импорт указывается после объявления пакета и до функций. Без него имя `fmt`
не определено.

## Несколько импортов

~~~go
import (
    "fmt"
    "strings"
)
~~~

Или отдельными строками:

~~~go
import "fmt"
import "strings"
~~~

## Лишний импорт — тоже ошибка

В Go нельзя импортировать пакет и не использовать его:

~~~text
"fmt" imported and not used
~~~

Это защита от «мусорных» зависимостей. Если пакет нужен только ради побочного
эффекта (например, драйвер БД), используют `_ "package/path"`.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| Нет импорта | `undefined: fmt` |
| Импорт после `func` | Синтаксическая ошибка |
| Неиспользуемый импорт | `imported and not used` |
@@TESTS
| *(нет ввода)* | `Imported!\n` |
@@CASES
run_case_devnull $'Imported!\n'
@@MAIN
package main

func main() {
	fmt.Println("Imported!")
}
@@SOLUTION
package main

import "fmt"

func main() {
	fmt.Println("Imported!")
}
@@COMMENTED
package main

import "fmt"

func main() {
	// fmt — стандартный пакет форматированного вывода.
	fmt.Println("Imported!")
}
@@END

@@TASK
section: 01_basics
dir: 04_variables_output
num: 1_4
title: GO_01_04. Переменные и вывод
topics: `var`, `:=`, `int`, `string`, `fmt.Printf`
input: Не требуются
@@DESC
Объяви две переменные:

- `name` типа `string` со значением `Gopher`;
- `age` типа `int` со значением `15`.

Выведи их в формате:

~~~text
Name: Gopher
Age: 15
~~~

Используй `fmt.Printf` с глаголами `%s` и `%d` или конкатенацию строк.
@@EXAMPLES
| *(нет ввода)* | `Name: Gopher`<br>`Age: 15` |
@@THEORY
## Объявление переменных

~~~go
var name string = "Gopher"
var age int = 15
~~~

Внутри функции можно использовать короткое объявление:

~~~go
name := "Gopher"
age := 15
~~~

Тип выводится из значения. `:=` работает только внутри функций.

## Типы

| Тип | Пример | Назначение |
| --- | --- | --- |
| `string` | `"Gopher"` | строка |
| `int` | `15` | целое число |
| `float64` | `3.14` | вещественное |
| `bool` | `true` | логическое |

## Форматированный вывод

~~~go
fmt.Printf("Name: %s\n", name)
fmt.Printf("Age: %d\n", age)
~~~

Глаголы: `%s` — строка, `%d` — целое, `%f` — вещественное, `%v` — значение
в формате по умолчанию, `%q` — строка в кавычках.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `%s` для числа | Странный вывод вида `%!s(int=15)` |
| Нет `\n` в `Printf` | Следующий вывод приклеится к текущему |
| Переменная объявлена и не использована | Ошибка компиляции |
@@TESTS
| *(нет ввода)* | `Name: Gopher\nAge: 15\n` |
@@CASES
run_case_devnull $'Name: Gopher\nAge: 15\n'
@@MAIN
package main

import "fmt"

func main() {
	name := "Gopher"
	age := 15
	// TODO: выведи Name: <name> и Age: <age> на отдельных строках
	_, _ = name, age
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	name := "Gopher"
	age := 15
	fmt.Printf("Name: %s\n", name)
	fmt.Printf("Age: %d\n", age)
}
@@COMMENTED
package main

import "fmt"

func main() {
	// := выводит тип из значения: string и int.
	name := "Gopher"
	age := 15
	fmt.Printf("Name: %s\n", name)
	fmt.Printf("Age: %d\n", age)
}
@@END

@@TASK
section: 01_basics
dir: 05_swap_two_numbers
num: 1_5
title: GO_01_05. Обмен значений
topics: `fmt.Scan`, множественное присваивание
input: Два целых числа через пробел
@@DESC
Считай два целых числа `a` и `b` и выведи их в обратном порядке.

В Go можно поменять значения местами одной строкой:

~~~go
a, b = b, a
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 3 5 | 5 3 |
| -1 7 | 7 -1 |
| 42 42 | 42 42 |
@@THEORY
## Чтение чисел

~~~go
var a, b int
fmt.Scan(&a, &b)
~~~

`Scan` читает значения, разделённые пробелами или переводами строк. Аргументы
передаются по указателю — поэтому перед именем переменной стоит `&`.

## Обмен значениями

В C для обмена нужна временная переменная. В Go достаточно множественного
присваивания:

~~~go
a, b = b, a
~~~

Правая часть вычисляется до присваивания, поэтому значения не теряются.

## Вывод

~~~go
fmt.Println(b, a)
~~~

`Println` разделяет аргументы пробелом и добавляет перевод строки.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `fmt.Scan(a, b)` | Передана копия, значения не читаются |
| `a = b; b = a` | Оба числа станут равны `b` |
| `fmt.Println(a, b)` | Числа не поменялись местами |
@@TESTS
| `3 5` | `5 3\n` |
| `-1 7` | `7 -1\n` |
| `0 0` | `0 0\n` |
| `42 42` | `42 42\n` |
@@CASES
run_case "3 5" $'5 3\n'
run_case "-1 7" $'7 -1\n'
run_case "0 0" $'0 0\n'
run_case "42 42" $'42 42\n'
run_case $'3\n5' $'5 3\n'
@@MAIN
package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	// TODO: выведи b и a через пробел
	fmt.Println(a, b)
}
@@SOLUTION
package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	fmt.Println(b, a)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var a, b int
	// Scan принимает указатели, поэтому нужен &.
	fmt.Scan(&a, &b)
	fmt.Println(b, a)
}
@@END

@@TASK
section: 02_input_output
dir: 01_echo_number
num: 2_1
title: GO_02_01. Эхо числа
topics: `fmt.Scan`, `fmt.Println`
input: Одно целое число
@@DESC
Считай целое число и выведи его без изменений.

Это первое задание на ввод: учимся читать число из стандартного потока.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 42 | 42 |
| -7 | -7 |
| 0 | 0 |
@@THEORY
## Стандартный ввод

`os.Stdin` — поток, из которого программа читает данные. Самый простой способ
прочитать число — `fmt.Scan`:

~~~go
var n int
fmt.Scan(&n)
~~~

## Указатель

`Scan` должен изменить переменную, поэтому принимает её адрес: `&n`. Если
передать `n` без `&`, программа не скомпилируется.

## Вывод

~~~go
fmt.Println(n)
~~~

## Что если ввода нет

`Scan` вернёт ошибку, а `n` останется нулём. В этом тренажёре для таких случаев
есть отдельные тесты: программа не должна падать с паникой.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `fmt.Scan(n)` | Ошибка компиляции |
| Забыть `var n int` | `undefined: n` |
| Читать строку через `Scan` | Для строки без пробелов это работает, но `\n` остаётся в потоке |
@@TESTS
| `42` | `42\n` |
| `-7` | `-7\n` |
| `0` | `0\n` |
@@CASES
run_case "42" $'42\n'
run_case "-7" $'-7\n'
run_case "0" $'0\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// TODO: выведи прочитанное число
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	fmt.Println(n)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var n int
	// &n — адрес переменной, куда Scan запишет число.
	fmt.Scan(&n)
	fmt.Println(n)
}
@@END

@@TASK
section: 02_input_output
dir: 02_sum_two_numbers
num: 2_2
title: GO_02_02. Сумма двух чисел
topics: `fmt.Scan`, арифметика
input: Два целых числа
@@DESC
Считай два целых числа и выведи их сумму.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 2 3 | 5 |
| -4 10 | 6 |
| 0 0 | 0 |
@@THEORY
## Чтение нескольких значений

~~~go
var a, b int
fmt.Scan(&a, &b)
~~~

`Scan` пропускает пробелы и переводы строк, поэтому числа могут быть на одной
строке или на разных.

## Арифметика

~~~go
sum := a + b
fmt.Println(sum)
~~~

Тип результата — `int`, как и у операндов.

## Переполнение

Целые в Go переполняются без исключения. На 64-битной платформе `int` — 64
бита, но для очень больших сумм лучше сразу брать `int64`.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `a + b` без `fmt.Println` | Результат вычислен, но не выведен |
| Один `&` на две переменные | Вторая останется нулём |
| Чтение `float64` через `Scan` в `int` | Ошибка несоответствия типа |
@@TESTS
| `2 3` | `5\n` |
| `-4 10` | `6\n` |
| `0 0` | `0\n` |
| `1000000 2000000` | `3000000\n` |
@@CASES
run_case "2 3" $'5\n'
run_case "-4 10" $'6\n'
run_case "0 0" $'0\n'
run_case "1000000 2000000" $'3000000\n'
run_case $'7\n8' $'15\n'
@@MAIN
package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	// TODO: выведи сумму a и b
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	fmt.Println(a + b)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	// Сумма двух int имеет тип int.
	fmt.Println(a + b)
}
@@END

@@TASK
section: 02_input_output
dir: 03_read_full_line
num: 2_3
title: GO_02_03. Чтение строки целиком
topics: `bufio.Scanner`, `os.Stdin`, `Scan`
input: Одна строка (может содержать пробелы)
@@DESC
Считай строку целиком, включая пробелы, и выведи её в формате:

~~~text
Line: <строка>
~~~

Для пустой строки вывод: `Line: ` (с пробелом после двоеточия, без текста).
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| hello world | Line: hello world |
| Go is fun | Line: Go is fun |
| *(пустая строка)* | Line: |
@@THEORY
## Почему не fmt.Scan

`fmt.Scan` читает **слово** до пробела. Для строки с пробелами нужен
`bufio.Scanner`:

~~~go
scanner := bufio.NewScanner(os.Stdin)
if scanner.Scan() {
    line := scanner.Text()
    fmt.Println("Line: " + line)
}
~~~

`Scan()` возвращает `false`, если ввода нет. `Text()` — прочитанную строку без
завершающего `\n`.

## Пустая строка

Пустая строка — это не отсутствие ввода. `Scan()` вернёт `true`, а `Text()` —
пустую строку, поэтому программа напечатает `Line: `.

## Ошибки сканера

~~~go
if err := scanner.Err(); err != nil {
    // ...
}
~~~

Для стандартного ввода ошибки редки, но проверять их — хорошая привычка.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `fmt.Scan(&line)` | Читает только первое слово |
| `scanner.Text()` до `Scan()` | Пустая строка |
| Забыт `bufio`/`os` в импортах | Ошибка компиляции |
@@TESTS
| `hello world` | `Line: hello world\n` |
| `Go is fun` | `Line: Go is fun\n` |
| *(пустая строка)* | `Line: \n` |
| `   ` | `Line:    \n` |
@@CASES
run_case "hello world" $'Line: hello world\n'
run_case "Go is fun" $'Line: Go is fun\n'
run_case "" $'Line: \n'
run_case "   " $'Line:    \n'
run_case_devnull ""
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
		// TODO: выведи "Line: " и строку line
		_ = line
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
		fmt.Println("Line: " + scanner.Text())
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
	// Scanner читает строку целиком до \n.
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		fmt.Println("Line: " + scanner.Text())
	}
}
@@END

@@TASK
section: 02_input_output
dir: 04_formatted_output
num: 2_4
title: GO_02_04. Форматированный вывод
topics: `fmt.Scan`, `float64`, `fmt.Printf`
input: Одно вещественное число
@@DESC
Считай вещественное число и выведи его с двумя знаками после точки:

~~~text
Value: 3.14
~~~

Используй `fmt.Printf` с глаголом `%.2f`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 3.14159 | Value: 3.14 |
| 2 | Value: 2.00 |
| -0.5 | Value: -0.50 |
@@THEORY
## Вещественные числа

~~~go
var x float64
fmt.Scan(&x)
~~~

В Go нет отдельного типа `double`: `float64` — обычный выбор для вещественных
чисел.

## Точность

~~~go
fmt.Printf("Value: %.2f\n", x)
~~~

`%.2f` печатает два знака после точки и округляет. `2` превращается в `2.00`.

## Локаль

В отличие от Java и C, `fmt` в Go всегда использует точку как десятичный
разделитель, независимо от локали системы. Поэтому тесты одинаковы на Windows
и Linux.

## Другие глаголы

| Глагол | Пример | Результат |
| --- | --- | --- |
| `%f` | `3.14` | `3.140000` |
| `%.2f` | `3.14159` | `3.14` |
| `%8.2f` | `3.14` | `    3.14` |
| `%v` | `3.14` | `3.14` |

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `var x int` для `3.14` | `Scan` не прочитает число |
| `%.2d` вместо `%.2f` | Неверный формат |
| Забыт `\n` | Следующий вывод окажется на той же строке |
@@TESTS
| `3.14159` | `Value: 3.14\n` |
| `2` | `Value: 2.00\n` |
| `-0.5` | `Value: -0.50\n` |
| `0` | `Value: 0.00\n` |
@@CASES
run_case "3.14159" $'Value: 3.14\n'
run_case "2" $'Value: 2.00\n'
run_case "-0.5" $'Value: -0.50\n'
run_case "0" $'Value: 0.00\n'
@@MAIN
package main

import "fmt"

func main() {
	var x float64
	fmt.Scan(&x)
	// TODO: выведи "Value: " и число с двумя знаками после точки
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var x float64
	fmt.Scan(&x)
	fmt.Printf("Value: %.2f\n", x)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var x float64
	fmt.Scan(&x)
	// %.2f — два знака после точки, округление стандартное.
	fmt.Printf("Value: %.2f\n", x)
}
@@END

@@TASK
section: 02_input_output
dir: 05_mixed_input
num: 2_5
title: GO_02_05. Число и строка
topics: `fmt.Scan`, разные типы в одном вводе
input: Имя и возраст через пробел
@@DESC
Считай имя (одно слово) и возраст, затем выведи:

~~~text
Hello, <имя>! You are <возраст>.
~~~

Например, для `Alice 30` результат:

~~~text
Hello, Alice! You are 30.
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| Alice 30 | Hello, Alice! You are 30. |
| Bob 7 | Hello, Bob! You are 7. |
| Gopher 1 | Hello, Gopher! You are 1. |
@@THEORY
## Разные типы в одном Scan

~~~go
var name string
var age int
fmt.Scan(&name, &age)
~~~

`Scan` читает значения по порядку и приводит их к типам аргументов. Строка
читается до пробела, число — до следующего разделителя.

## Строка с пробелами

Если имя может содержать пробел (`Mary Jane`), `Scan` прочитает только `Mary`.
Для таких случаев нужен `bufio.Scanner` и отдельный разбор строки.

## Сборка вывода

~~~go
fmt.Printf("Hello, %s! You are %d.\n", name, age)
~~~

Знаки препинания — часть формата, их нужно расставить точно: автотест сравнивает
вывод побайтово.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| Возраст объявлен как `string` | Вывод с `%d` даст `%!d(string=...)` |
| Нет `&` у одной из переменных | Переменная останется пустой/нулём |
| Лишняя точка или пробел | Тест не пройден |
@@TESTS
| `Alice 30` | `Hello, Alice! You are 30.\n` |
| `Bob 7` | `Hello, Bob! You are 7.\n` |
| `Gopher 1` | `Hello, Gopher! You are 1.\n` |
| `X 0` | `Hello, X! You are 0.\n` |
@@CASES
run_case "Alice 30" $'Hello, Alice! You are 30.\n'
run_case "Bob 7" $'Hello, Bob! You are 7.\n'
run_case "Gopher 1" $'Hello, Gopher! You are 1.\n'
run_case "X 0" $'Hello, X! You are 0.\n'
@@MAIN
package main

import "fmt"

func main() {
	var name string
	var age int
	fmt.Scan(&name, &age)
	// TODO: выведи Hello, <name>! You are <age>.
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var name string
	var age int
	fmt.Scan(&name, &age)
	fmt.Printf("Hello, %s! You are %d.\n", name, age)
}
@@COMMENTED
package main

import "fmt"

func main() {
	var name string
	var age int
	// Scan читает string и int по очереди.
	fmt.Scan(&name, &age)
	fmt.Printf("Hello, %s! You are %d.\n", name, age)
}
@@END
