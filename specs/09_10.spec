@@TASK
section: 09_errors
dir: 01_safe_division
num: 9_1
title: GO_09_01. Безопасное деление
topics: `error`, `errors.New`, множественный возврат
input: Два целых числа A и B
@@DESC
Напиши функцию `Divide(a, b int) (int, error)`. Если `b == 0`, верни ошибку
`division by zero`. Иначе верни результат и `nil`.
Выведи `Result: ...` или `Error: division by zero`.

~~~text
Result: 5
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 10 2 | Result: 5 |
| 5 0 | Error: division by zero |
@@THEORY
## Ошибка — обычное значение

~~~go
func Divide(a, b int) (int, error) {
    if b == 0 {
        return 0, errors.New("division by zero")
    }
    return a / b, nil
}
~~~

В Go нет исключений. Функция возвращает результат **и** ошибку. Если ошибки
нет — возвращается `nil`.

## Проверка

~~~go
result, err := Divide(a, b)
if err != nil {
    fmt.Println("Error:", err)
} else {
    fmt.Printf("Result: %d\n", result)
}
~~~

Сначала проверяем `err`, только потом используем результат.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| Игнорировать `err` | При делении на ноль программа упадёт |
| `if err == nil` для ошибки | Логика перевёрнута |
| `errors.New` без импорта | Ошибка компиляции |
@@TESTS
| `10 2` | `Result: 5\n` |
| `5 0` | `Error: division by zero\n` |
| `-9 3` | `Result: -3\n` |
| `0 7` | `Result: 0\n` |
@@CASES
run_case "10 2" $'Result: 5\n'
run_case "5 0" $'Error: division by zero\n'
run_case "-9 3" $'Result: -3\n'
run_case "0 7" $'Result: 0\n'
@@MAIN
package main

import (
	"errors"
	"fmt"
)

// TODO: реализуй Divide
func Divide(a, b int) (int, error) {
	return 0, errors.New("not implemented")
}

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	result, err := Divide(a, b)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Printf("Result: %d\n", result)
	}
}
@@SOLUTION
package main

import (
	"errors"
	"fmt"
)

func Divide(a, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("division by zero")
	}
	return a / b, nil
}

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	result, err := Divide(a, b)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Printf("Result: %d\n", result)
	}
}
@@COMMENTED
package main

import (
	"errors"
	"fmt"
)

// Divide возвращает результат и ошибку: в Go ошибка — обычное значение.
func Divide(a, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("division by zero")
	}
	return a / b, nil
}

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	result, err := Divide(a, b)
	// Сначала проверяем err, потом используем result.
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Printf("Result: %d\n", result)
	}
}
@@END

@@TASK
section: 09_errors
dir: 02_parse_int
num: 9_2
title: GO_09_02. Разбор числа
topics: `strconv.Atoi`, проверка ошибки
input: Одно слово
@@DESC
Считай строку и попробуй превратить её в целое число через `strconv.Atoi`.
Если получилось — выведи `Number: ...`, иначе — `Invalid number`.

~~~text
Number: 42
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 42 | Number: 42 |
| abc | Invalid number |
@@THEORY
## strconv.Atoi

~~~go
n, err := strconv.Atoi("42")  // n == 42, err == nil
m, err := strconv.Atoi("abc") // m == 0, err != nil
~~~

`Atoi` расшифровывается как ASCII to integer.

## Обработка

~~~go
if err != nil {
    fmt.Println("Invalid number")
} else {
    fmt.Printf("Number: %d\n", n)
}
~~~

Даже при ошибке `n` содержит `0`, но использовать его нельзя — это не
результат разбора.

## Связанные функции

| Функция | Назначение |
| --- | --- |
| `strconv.Itoa(42)` | Число в строку |
| `strconv.ParseFloat` | Строка в `float64` |
| `strconv.Atoi` | Строка в `int` |
@@TESTS
| `42` | `Number: 42\n` |
| `abc` | `Invalid number\n` |
| `-7` | `Number: -7\n` |
| `3.5` | `Invalid number\n` |
@@CASES
run_case "42" $'Number: 42\n'
run_case "abc" $'Invalid number\n'
run_case "-7" $'Number: -7\n'
run_case "3.5" $'Invalid number\n'
@@MAIN
package main

import (
	"fmt"
	"strconv"
)

func main() {
	var s string
	fmt.Scan(&s)
	n, err := strconv.Atoi(s)
	// TODO: выведи число или сообщение об ошибке
	_ = n
	_ = err
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"fmt"
	"strconv"
)

func main() {
	var s string
	fmt.Scan(&s)
	n, err := strconv.Atoi(s)
	if err != nil {
		fmt.Println("Invalid number")
	} else {
		fmt.Printf("Number: %d\n", n)
	}
}
@@COMMENTED
package main

import (
	"fmt"
	"strconv"
)

func main() {
	var s string
	fmt.Scan(&s)
	n, err := strconv.Atoi(s)
	// err != nil означает, что строку не удалось разобрать.
	if err != nil {
		fmt.Println("Invalid number")
	} else {
		fmt.Printf("Number: %d\n", n)
	}
}
@@END

@@TASK
section: 09_errors
dir: 03_custom_error
num: 9_3
title: GO_09_03. Своя ошибка
topics: тип-ошибка, `Error()`, `errors.As`
input: Возраст одним числом
@@DESC
Объяви тип `ValidationError` с полем `Field` и методом `Error() string`.
Функция `ValidateAge(age int) error` возвращает `&ValidationError{Field: "age"}`,
если возраст отрицательный. Выведи `Age: ...` или `Validation error: age`.

~~~text
Validation error: age
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| -1 | Validation error: age |
| 20 | Age: 20 |
@@THEORY
## Свой тип ошибки

~~~go
type ValidationError struct {
    Field string
}

func (e *ValidationError) Error() string {
    return "validation failed: " + e.Field
}
~~~

Любой тип с методом `Error() string` является ошибкой.

## Возврат

~~~go
func ValidateAge(age int) error {
    if age < 0 {
        return &ValidationError{Field: "age"}
    }
    return nil
}
~~~

Возвращаем указатель, потому что метод объявлен на `*ValidationError`.

## Достать конкретный тип

~~~go
var ve *ValidationError
if errors.As(err, &ve) {
    fmt.Println("Validation error:", ve.Field)
}
~~~

`errors.As` ищет ошибку нужного типа в цепочке обёрнутых ошибок.
@@TESTS
| `-1` | `Validation error: age\n` |
| `20` | `Age: 20\n` |
| `0` | `Age: 0\n` |
| `-100` | `Validation error: age\n` |
@@CASES
run_case "-1" $'Validation error: age\n'
run_case "20" $'Age: 20\n'
run_case "0" $'Age: 0\n'
run_case "-100" $'Validation error: age\n'
@@MAIN
package main

import (
	"errors"
	"fmt"
)

// TODO: объяви ValidationError и ValidateAge

type ValidationError struct {
	Field string
}

func (e *ValidationError) Error() string {
	return "validation failed: " + e.Field
}

func ValidateAge(age int) error {
	return nil
}

func main() {
	var age int
	fmt.Scan(&age)
	err := ValidateAge(age)
	if err != nil {
		var ve *ValidationError
		if errors.As(err, &ve) {
			fmt.Println("Validation error:", ve.Field)
		}
	} else {
		fmt.Printf("Age: %d\n", age)
	}
}
@@SOLUTION
package main

import (
	"errors"
	"fmt"
)

type ValidationError struct {
	Field string
}

func (e *ValidationError) Error() string {
	return "validation failed: " + e.Field
}

func ValidateAge(age int) error {
	if age < 0 {
		return &ValidationError{Field: "age"}
	}
	return nil
}

func main() {
	var age int
	fmt.Scan(&age)
	err := ValidateAge(age)
	if err != nil {
		var ve *ValidationError
		if errors.As(err, &ve) {
			fmt.Println("Validation error:", ve.Field)
		}
	} else {
		fmt.Printf("Age: %d\n", age)
	}
}
@@COMMENTED
package main

import (
	"errors"
	"fmt"
)

// ValidationError — своя ошибка: достаточно метода Error() string.
type ValidationError struct {
	Field string
}

func (e *ValidationError) Error() string {
	return "validation failed: " + e.Field
}

func ValidateAge(age int) error {
	if age < 0 {
		return &ValidationError{Field: "age"}
	}
	return nil
}

func main() {
	var age int
	fmt.Scan(&age)
	err := ValidateAge(age)
	if err != nil {
		// errors.As достаёт конкретный тип из ошибки.
		var ve *ValidationError
		if errors.As(err, &ve) {
			fmt.Println("Validation error:", ve.Field)
		}
	} else {
		fmt.Printf("Age: %d\n", age)
	}
}
@@END

@@TASK
section: 09_errors
dir: 04_defer
num: 9_4
title: GO_09_04. Порядок defer
topics: `defer`, порядок выполнения
input: Одно слово
@@DESC
Напиши функцию `process(word string)`, которая печатает:

~~~text
open <word>
work
close
~~~

Строка `close` должна выводиться через `defer`, чтобы она выполнилась
последней.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| hive | open hive<br>work<br>close |
| go | open go<br>work<br>close |
@@THEORY
## defer

~~~go
func process(word string) {
    defer fmt.Println("close")
    fmt.Println("open " + word)
    fmt.Println("work")
}
~~~

`defer` откладывает вызов до выхода из функции. Несколько `defer` выполняются
в обратном порядке (LIFO).

## Когда полезно

- закрыть файл: `defer f.Close()`;
- освободить ресурс;
- вывести итог после работы.

## Порядок

~~~go
func demo() {
    defer fmt.Println("1")
    defer fmt.Println("2")
    fmt.Println("body")
}
// body, 2, 1
~~~

Аргументы отложенного вызова вычисляются сразу, а вызов происходит позже.
@@TESTS
| `hive` | `open hive\nwork\nclose\n` |
| `go` | `open go\nwork\nclose\n` |
| `x` | `open x\nwork\nclose\n` |
@@CASES
run_case "hive" $'open hive\nwork\nclose\n'
run_case "go" $'open go\nwork\nclose\n'
run_case "x" $'open x\nwork\nclose\n'
@@MAIN
package main

import "fmt"

func process(word string) {
	// TODO: добавь defer для close и вывод open/work
	fmt.Println("TODO")
}

func main() {
	var word string
	fmt.Scan(&word)
	process(word)
}
@@SOLUTION
package main

import "fmt"

func process(word string) {
	defer fmt.Println("close")
	fmt.Println("open " + word)
	fmt.Println("work")
}

func main() {
	var word string
	fmt.Scan(&word)
	process(word)
}
@@COMMENTED
package main

import "fmt"

func process(word string) {
	// close выполнится последним, когда process завершится.
	defer fmt.Println("close")
	fmt.Println("open " + word)
	fmt.Println("work")
}

func main() {
	var word string
	fmt.Scan(&word)
	process(word)
}
@@END

@@TASK
section: 09_errors
dir: 05_panic_recover
num: 9_5
title: GO_09_05. panic и recover
topics: `panic`, `recover`, отложенная функция
input: Два целых числа A и B
@@DESC
Напиши `SafeDivide(a, b int) (int, error)`. При `b == 0` вызови
`panic("division by zero")`, перехвати панику через `recover` в `defer`
и верни её как ошибку. Выведи `Result: ...` или `Recovered: division by zero`.

~~~text
Recovered: division by zero
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 10 2 | Result: 5 |
| 5 0 | Recovered: division by zero |
@@THEORY
## panic

~~~go
panic("division by zero")
~~~

Паника останавливает обычное выполнение и раскручивает стек.

## recover

~~~go
func SafeDivide(a, b int) (result int, err error) {
    defer func() {
        if r := recover(); r != nil {
            err = fmt.Errorf("%v", r)
        }
    }()
    if b == 0 {
        panic("division by zero")
    }
    return a / b, nil
}
~~~

`recover` работает только внутри `defer`. Он возвращает значение паники
или `nil`, если паники не было.

## Именованный результат

`(result int, err error)` позволяет `defer` записать значение в `err` после
возврата из функции.

## Важно

`panic` — не замена ошибкам. В обычном коде возвращай `error`, а `recover`
используй на границах программы.
@@TESTS
| `10 2` | `Result: 5\n` |
| `5 0` | `Recovered: division by zero\n` |
| `0 4` | `Result: 0\n` |
| `-8 2` | `Result: -4\n` |
@@CASES
run_case "10 2" $'Result: 5\n'
run_case "5 0" $'Recovered: division by zero\n'
run_case "0 4" $'Result: 0\n'
run_case "-8 2" $'Result: -4\n'
@@MAIN
package main

import "fmt"

// TODO: реализуй SafeDivide с panic и recover
func SafeDivide(a, b int) (int, error) {
	return 0, nil
}

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	result, err := SafeDivide(a, b)
	if err != nil {
		fmt.Println("Recovered:", err)
	} else {
		fmt.Printf("Result: %d\n", result)
	}
}
@@SOLUTION
package main

import "fmt"

func SafeDivide(a, b int) (result int, err error) {
	defer func() {
		if r := recover(); r != nil {
			err = fmt.Errorf("%v", r)
		}
	}()
	if b == 0 {
		panic("division by zero")
	}
	return a / b, nil
}

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	result, err := SafeDivide(a, b)
	if err != nil {
		fmt.Println("Recovered:", err)
	} else {
		fmt.Printf("Result: %d\n", result)
	}
}
@@COMMENTED
package main

import "fmt"

// SafeDivide перехватывает собственную панику и превращает её в ошибку.
func SafeDivide(a, b int) (result int, err error) {
	defer func() {
		// recover() возвращает значение panic или nil.
		if r := recover(); r != nil {
			err = fmt.Errorf("%v", r)
		}
	}()
	if b == 0 {
		panic("division by zero")
	}
	return a / b, nil
}

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	result, err := SafeDivide(a, b)
	if err != nil {
		fmt.Println("Recovered:", err)
	} else {
		fmt.Printf("Result: %d\n", result)
	}
}
@@END

@@TASK
section: 10_files
dir: 01_read_file
num: 10_1
title: GO_10_01. Чтение файла
topics: `os.ReadFile`, обработка ошибки
input: Имя файла
@@DESC
Считай имя файла, прочитай его через `os.ReadFile` и выведи содержимое
без изменений. Если файла нет — выведи `Error: cannot read file`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| data.txt (содержит `hello`) | hello |
| missing.txt | Error: cannot read file |
@@THEORY
## os.ReadFile

~~~go
data, err := os.ReadFile(name)
if err != nil {
    fmt.Println("Error: cannot read file")
    return
}
fmt.Print(string(data))
~~~

Функция возвращает `[]byte`. `string(data)` превращает байты в строку.

## Print или Println

- `fmt.Print` — без добавления перевода строки;
- `fmt.Println` — добавляет `\n`.

Если файл уже заканчивается переводом строки, `Print` сохранит его как есть.

## Учебные файлы в тестах

Автотест создаёт `f1.txt` командой `printf` и передаёт его имя программе.
@@TESTS
| `f1.txt` (`hello\nworld\n`) | `hello\nworld\n` |
| `f1.txt` (`abc`) | `abc` |
| `missing.txt` | `Error: cannot read file\n` |
@@CASES
trap 'rm -f f1.txt missing.txt' EXIT
printf 'hello\nworld\n' > f1.txt
run_case "f1.txt" $'hello\nworld\n'
printf 'abc' > f1.txt
run_case "f1.txt" "abc"
run_case "missing.txt" $'Error: cannot read file\n'
@@MAIN
package main

import "fmt"

func main() {
	var name string
	fmt.Scan(&name)
	// TODO: прочитай файл и выведи содержимое
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"fmt"
	"os"
)

func main() {
	var name string
	fmt.Scan(&name)
	data, err := os.ReadFile(name)
	if err != nil {
		fmt.Println("Error: cannot read file")
		return
	}
	fmt.Print(string(data))
}
@@COMMENTED
package main

import (
	"fmt"
	"os"
)

func main() {
	var name string
	fmt.Scan(&name)
	data, err := os.ReadFile(name)
	if err != nil {
		fmt.Println("Error: cannot read file")
		return
	}
	// data — []byte; Print не добавляет лишний перевод строки.
	fmt.Print(string(data))
}
@@END

@@TASK
section: 10_files
dir: 02_write_file
num: 10_2
title: GO_10_02. Запись файла
topics: `os.WriteFile`, права доступа, чтение после записи
input: Имя файла и строка
@@DESC
Считай имя файла и слово. Запиши слово в файл с переводом строки.
Затем прочитай файл обратно и выведи `Saved: <слово>`.

~~~text
Saved: hello
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| out.txt hello | Saved: hello |
@@THEORY
## os.WriteFile

~~~go
content := line + "\n"
err := os.WriteFile(name, []byte(content), 0644)
~~~

Третий аргумент — права доступа (как в Unix). `0644` означает: владелец
читает и пишет, остальные только читают.

`[]byte(content)` превращает строку в срез байтов.

## Проверка ошибки

~~~go
if err != nil {
    fmt.Println("Error: cannot write file")
    return
}
~~~

## Чтение обратно

~~~go
data, err := os.ReadFile(name)
fmt.Println("Saved: " + strings.TrimSpace(string(data)))
~~~

`TrimSpace` убирает перевод строки, который мы сами записали.
@@TESTS
| `out.txt hello` | `Saved: hello\n` |
| `out.txt Go` | `Saved: Go\n` |
@@CASES
trap 'rm -f out.txt' EXIT
run_case "out.txt hello" $'Saved: hello\n'
diff <(printf 'hello\n') out.txt
run_case "out.txt Go" $'Saved: Go\n'
diff <(printf 'Go\n') out.txt
@@MAIN
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var name, word string
	fmt.Scan(&name, &word)
	// TODO: запиши word с переводом строки и прочитай обратно
	_ = os.WriteFile
	_ = strings.TrimSpace
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var name, word string
	fmt.Scan(&name, &word)
	content := word + "\n"
	if err := os.WriteFile(name, []byte(content), 0644); err != nil {
		fmt.Println("Error: cannot write file")
		return
	}
	data, err := os.ReadFile(name)
	if err != nil {
		fmt.Println("Error: cannot read file")
		return
	}
	fmt.Println("Saved: " + strings.TrimSpace(string(data)))
}
@@COMMENTED
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var name, word string
	fmt.Scan(&name, &word)

	content := word + "\n"
	// 0644 — права на чтение/запись для владельца, чтение для остальных.
	if err := os.WriteFile(name, []byte(content), 0644); err != nil {
		fmt.Println("Error: cannot write file")
		return
	}

	data, err := os.ReadFile(name)
	if err != nil {
		fmt.Println("Error: cannot read file")
		return
	}
	fmt.Println("Saved: " + strings.TrimSpace(string(data)))
}
@@END

@@TASK
section: 10_files
dir: 03_copy_file
num: 10_3
title: GO_10_03. Копирование файла
topics: чтение и запись, `os.ReadFile`, `os.WriteFile`
input: Имя исходного файла и имя копии
@@DESC
Считай два имени файла. Скопируй содержимое первого во второй и выведи
`Copied: <содержимое без последнего перевода строки>`.
Если исходный файл не читается — выведи `Error: cannot read source`.

~~~text
Copied: hello
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| f1.txt f2.txt (в f1: `hello`) | Copied: hello |
| missing.txt f2.txt | Error: cannot read source |
@@THEORY
## Копирование

~~~go
data, err := os.ReadFile(src)
if err != nil {
    fmt.Println("Error: cannot read source")
    return
}
err = os.WriteFile(dst, data, 0644)
~~~

Байты не нужно преобразовывать: `ReadFile` вернул `[]byte`, `WriteFile` его
принимает.

## Вывод содержимого

~~~go
fmt.Printf("Copied: %s\n", strings.TrimSpace(string(data)))
~~~

`TrimSpace` убирает пробелы и переводы строк по краям.

## Порядок проверок

Сначала читаем источник, потом пишем копию. Иначе при ошибке чтения можно
создать пустой файл назначения.
@@TESTS
| `f1.txt f2.txt` (`hello\n`) | `Copied: hello\n` |
| `f1.txt f2.txt` (`a b\n`) | `Copied: a b\n` |
| `missing.txt f2.txt` | `Error: cannot read source\n` |
@@CASES
trap 'rm -f f1.txt f2.txt' EXIT
printf 'hello\n' > f1.txt
run_case "f1.txt f2.txt" $'Copied: hello\n'
diff f1.txt f2.txt
printf 'a b\n' > f1.txt
run_case "f1.txt f2.txt" $'Copied: a b\n'
diff f1.txt f2.txt
run_case "missing.txt f2.txt" $'Error: cannot read source\n'
@@MAIN
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var src, dst string
	fmt.Scan(&src, &dst)
	// TODO: скопируй src в dst и выведи содержимое
	_ = os.ReadFile
	_ = strings.TrimSpace
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var src, dst string
	fmt.Scan(&src, &dst)
	data, err := os.ReadFile(src)
	if err != nil {
		fmt.Println("Error: cannot read source")
		return
	}
	if err := os.WriteFile(dst, data, 0644); err != nil {
		fmt.Println("Error: cannot write destination")
		return
	}
	fmt.Printf("Copied: %s\n", strings.TrimSpace(string(data)))
}
@@COMMENTED
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var src, dst string
	fmt.Scan(&src, &dst)

	// Сначала читаем источник: при ошибке файл назначения не создаём.
	data, err := os.ReadFile(src)
	if err != nil {
		fmt.Println("Error: cannot read source")
		return
	}
	if err := os.WriteFile(dst, data, 0644); err != nil {
		fmt.Println("Error: cannot write destination")
		return
	}
	fmt.Printf("Copied: %s\n", strings.TrimSpace(string(data)))
}
@@END

@@TASK
section: 10_files
dir: 04_sum_numbers_file
num: 10_4
title: GO_10_04. Сумма чисел из файла
topics: файлы, `strings.Fields`, `strconv.Atoi`
input: Имя файла с числами
@@DESC
Прочитай файл, в котором числа разделены пробелами и переводами строк.
Выведи их сумму: `Sum: ...`. Пустой файл даёт `Sum: 0`.

~~~text
Sum: 6
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| numbers.txt (`1 2 3\n`) | Sum: 6 |
| empty.txt | Sum: 0 |
@@THEORY
## Разбор файла

~~~go
data, err := os.ReadFile(name)
if err != nil {
    fmt.Println("Error: cannot read file")
    return
}
fields := strings.Fields(string(data))
~~~

`Fields` разбивает по любым пробельным символам, поэтому числа могут быть
на разных строках.

## Преобразование и сумма

~~~go
sum := 0
for _, f := range fields {
    n, err := strconv.Atoi(f)
    if err != nil {
        continue
    }
    sum += n
}
fmt.Printf("Sum: %d\n", sum)
~~~

## Крайний случай

Для пустого файла `Fields` вернёт пустой срез, цикл не выполнится, сумма
останется `0`.
@@TESTS
| `numbers.txt` (`1 2 3\n`) | `Sum: 6\n` |
| `empty.txt` | `Sum: 0\n` |
| `numbers.txt` (`10\n-5\n2`) | `Sum: 7\n` |
@@CASES
trap 'rm -f numbers.txt empty.txt' EXIT
printf '1 2 3\n' > numbers.txt
run_case "numbers.txt" $'Sum: 6\n'
: > empty.txt
run_case "empty.txt" $'Sum: 0\n'
printf '10\n-5\n2' > numbers.txt
run_case "numbers.txt" $'Sum: 7\n'
@@MAIN
package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var name string
	fmt.Scan(&name)
	// TODO: прочитай файл и посчитай сумму
	_ = os.ReadFile
	_ = strconv.Atoi
	_ = strings.Fields
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var name string
	fmt.Scan(&name)
	data, err := os.ReadFile(name)
	if err != nil {
		fmt.Println("Error: cannot read file")
		return
	}
	sum := 0
	for _, field := range strings.Fields(string(data)) {
		n, err := strconv.Atoi(field)
		if err != nil {
			continue
		}
		sum += n
	}
	fmt.Printf("Sum: %d\n", sum)
}
@@COMMENTED
package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var name string
	fmt.Scan(&name)
	data, err := os.ReadFile(name)
	if err != nil {
		fmt.Println("Error: cannot read file")
		return
	}

	sum := 0
	// Fields сам разбирается с пробелами и переводами строк.
	for _, field := range strings.Fields(string(data)) {
		n, err := strconv.Atoi(field)
		if err != nil {
			continue
		}
		sum += n
	}
	fmt.Printf("Sum: %d\n", sum)
}
@@END

@@TASK
section: 10_files
dir: 05_count_words_file
num: 10_5
title: GO_10_05. Слова в файле
topics: файлы, `strings.Fields`, `len`
input: Имя файла
@@DESC
Прочитай файл и посчитай количество слов в нём. Слова разделены пробелами,
табами и переводами строк. Выведи `Words: ...`.

~~~text
Words: 3
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| text.txt (`one two\nthree\n`) | Words: 3 |
| empty.txt | Words: 0 |
@@THEORY
## От файла к словам

~~~go
data, err := os.ReadFile(name)
if err != nil {
    fmt.Println("Error: cannot read file")
    return
}
words := strings.Fields(string(data))
fmt.Printf("Words: %d\n", len(words))
~~~

`Fields` — самый простой способ посчитать слова: он не создаёт пустых
элементов из повторных пробелов.

## Сравнение подходов

| Подход | Поведение |
| --- | --- |
| `strings.Fields` | Любые пробельные символы |
| `strings.Split(s, " ")` | Только пробел, пустые элементы |
| `len(data)` | Байты, а не слова |

## Проверка ошибки

Не забывай `return` после сообщения об ошибке, иначе программа продолжит
работать с пустыми данными.
@@TESTS
| `text.txt` (`one two\nthree\n`) | `Words: 3\n` |
| `empty.txt` | `Words: 0\n` |
| `text.txt` (`a`) | `Words: 1\n` |
@@CASES
trap 'rm -f text.txt empty.txt' EXIT
printf 'one two\nthree\n' > text.txt
run_case "text.txt" $'Words: 3\n'
: > empty.txt
run_case "empty.txt" $'Words: 0\n'
printf 'a' > text.txt
run_case "text.txt" $'Words: 1\n'
@@MAIN
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var name string
	fmt.Scan(&name)
	// TODO: прочитай файл и посчитай слова
	_ = os.ReadFile
	_ = strings.Fields
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var name string
	fmt.Scan(&name)
	data, err := os.ReadFile(name)
	if err != nil {
		fmt.Println("Error: cannot read file")
		return
	}
	words := strings.Fields(string(data))
	fmt.Printf("Words: %d\n", len(words))
}
@@COMMENTED
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var name string
	fmt.Scan(&name)
	data, err := os.ReadFile(name)
	if err != nil {
		fmt.Println("Error: cannot read file")
		return
	}
	// Fields игнорирует повторные пробелы и переводы строк.
	words := strings.Fields(string(data))
	fmt.Printf("Words: %d\n", len(words))
}
@@END

@@TASK
section: 10_files
dir: 06_file_stats
num: 10_6
title: GO_10_06. Статистика файла
topics: файлы, подсчёт строк и байтов
input: Имя файла
@@DESC
Прочитай файл и выведи две строки: количество строк и количество байтов.

~~~text
Lines: 2
Bytes: 4
~~~

Файл `a\nb\n` содержит две строки и четыре байта. Пустой файл даёт нули.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| f.txt (`a\nb\n`) | Lines: 2<br>Bytes: 4 |
| empty.txt | Lines: 0<br>Bytes: 0 |
@@THEORY
## Байты

~~~go
data, err := os.ReadFile(name)
fmt.Println(len(data))
~~~

`len([]byte)` — количество байтов. Для ASCII один символ равен одному байту,
для кириллицы — двум.

## Строки

~~~go
text := string(data)
text = strings.TrimSuffix(text, "\n")
lines := 0
if text != "" {
    lines = len(strings.Split(text, "\n"))
}
~~~

Сначала убираем последний перевод строки, чтобы `a\nb\n` дало две строки,
а не три. Пустой файл обрабатываем отдельно.

## Альтернатива

~~~go
lines := strings.Count(string(data), "\n")
if len(data) > 0 && !strings.HasSuffix(string(data), "\n") {
    lines++
}
~~~
@@TESTS
| `f.txt` (`a\nb\n`) | `Lines: 2\nBytes: 4\n` |
| `empty.txt` | `Lines: 0\nBytes: 0\n` |
| `f.txt` (`hello`) | `Lines: 1\nBytes: 5\n` |
| `f.txt` (`x\ny`) | `Lines: 2\nBytes: 3\n` |
@@CASES
trap 'rm -f f.txt empty.txt' EXIT
printf 'a\nb\n' > f.txt
run_case "f.txt" $'Lines: 2\nBytes: 4\n'
: > empty.txt
run_case "empty.txt" $'Lines: 0\nBytes: 0\n'
printf 'hello' > f.txt
run_case "f.txt" $'Lines: 1\nBytes: 5\n'
printf 'x\ny' > f.txt
run_case "f.txt" $'Lines: 2\nBytes: 3\n'
@@MAIN
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var name string
	fmt.Scan(&name)
	// TODO: посчитай строки и байты
	_ = os.ReadFile
	_ = strings.TrimSuffix
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var name string
	fmt.Scan(&name)
	data, err := os.ReadFile(name)
	if err != nil {
		fmt.Println("Error: cannot read file")
		return
	}
	bytes := len(data)
	text := strings.TrimSuffix(string(data), "\n")
	lines := 0
	if text != "" {
		lines = len(strings.Split(text, "\n"))
	}
	fmt.Printf("Lines: %d\n", lines)
	fmt.Printf("Bytes: %d\n", bytes)
}
@@COMMENTED
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var name string
	fmt.Scan(&name)
	data, err := os.ReadFile(name)
	if err != nil {
		fmt.Println("Error: cannot read file")
		return
	}

	bytes := len(data)
	// Убираем последний \n, иначе a\nb\n даст три строки.
	text := strings.TrimSuffix(string(data), "\n")
	lines := 0
	if text != "" {
		lines = len(strings.Split(text, "\n"))
	}
	fmt.Printf("Lines: %d\n", lines)
	fmt.Printf("Bytes: %d\n", bytes)
}
@@END
