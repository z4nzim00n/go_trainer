@@TASK
section: 13_advanced
dir: 01_reflection_fields
num: 13_1
title: GO_13_01. Поля через reflection
topics: `reflect`, `NumField`, `Type`
input: Имя и возраст
@@DESC
Опиши структуру `Person` с полями `Name string` и `Age int`.
Считай значения и выведи все поля через reflection в формате
`Имя=значение`, разделяя пробелом:

~~~text
Name=Alice Age=30
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| Alice 30 | Name=Alice Age=30 |
| Bob 0 | Name=Bob Age=0 |
@@THEORY
## reflect.Type и reflect.Value

~~~go
v := reflect.ValueOf(p)
t := v.Type()
fmt.Println(t.NumField())
~~~

`reflect.TypeOf` и `reflect.ValueOf` дают описание типа и значения во время
выполнения.

## Обход полей

~~~go
for i := 0; i < t.NumField(); i++ {
    field := t.Field(i)
    value := v.Field(i)
    fmt.Println(field.Name, value.Interface())
}
~~~

`Field(i)` у типа возвращает метаданные, у значения — само значение.

## Interface()

`value.Interface()` возвращает значение как `interface{}`, чтобы его можно
было напечатать через `%v`.

## Когда нужно

Reflection пригодится для сериализации, валидации и обобщённых библиотек.
В обычном коде старайся обходиться без него: он медленнее и менее безопасен.
@@TESTS
| `Alice 30` | `Name=Alice Age=30\n` |
| `Bob 0` | `Name=Bob Age=0\n` |
| `Eve -1` | `Name=Eve Age=-1\n` |
@@CASES
run_case "Alice 30" $'Name=Alice Age=30\n'
run_case "Bob 0" $'Name=Bob Age=0\n'
run_case "Eve -1" $'Name=Eve Age=-1\n'
@@MAIN
package main

import "fmt"

type Person struct {
	Name string
	Age  int
}

func main() {
	var p Person
	fmt.Scan(&p.Name, &p.Age)
	// TODO: выведи поля через reflection
	_ = p
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"fmt"
	"reflect"
	"strings"
)

type Person struct {
	Name string
	Age  int
}

func main() {
	var p Person
	fmt.Scan(&p.Name, &p.Age)

	v := reflect.ValueOf(p)
	t := v.Type()
	parts := make([]string, 0, t.NumField())
	for i := 0; i < t.NumField(); i++ {
		parts = append(parts, t.Field(i).Name+"="+fmt.Sprint(v.Field(i).Interface()))
	}
	fmt.Println(strings.Join(parts, " "))
}
@@COMMENTED
package main

import (
	"fmt"
	"reflect"
	"strings"
)

type Person struct {
	Name string
	Age  int
}

func main() {
	var p Person
	fmt.Scan(&p.Name, &p.Age)

	v := reflect.ValueOf(p) // значение
	t := v.Type()           // описание типа
	parts := make([]string, 0, t.NumField())
	for i := 0; i < t.NumField(); i++ {
		// t.Field(i) — имя и тип поля, v.Field(i) — его значение.
		parts = append(parts, t.Field(i).Name+"="+fmt.Sprint(v.Field(i).Interface()))
	}
	fmt.Println(strings.Join(parts, " "))
}
@@END

@@TASK
section: 13_advanced
dir: 02_reflection_invoke
num: 13_2
title: GO_13_02. Вызов метода через reflection
topics: `reflect.Value`, `MethodByName`, `Call`
input: Два целых числа
@@DESC
Опиши структуру `Calculator` с методом `Add(a, b int) int`.
Вызови метод через reflection и выведи результат:

~~~text
Result: 5
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 2 3 | Result: 5 |
| -1 1 | Result: 0 |
@@THEORY
## Поиск метода

~~~go
c := Calculator{}
m := reflect.ValueOf(c).MethodByName("Add")
~~~

`MethodByName` возвращает `reflect.Value`, который можно вызвать.

## Call

~~~go
args := []reflect.Value{
    reflect.ValueOf(a),
    reflect.ValueOf(b),
}
out := m.Call(args)
~~~

`Call` принимает срез значений и возвращает срез результатов.

## Результат

~~~go
fmt.Println(out[0].Int())
~~~

Для `int` используем `Int()`, для `string` — `String()`, для `float64` —
`Float()`.

## Осторожно

Если метода нет, `MethodByName` вернёт нулевое значение, а `Call` запаникует.
В реальном коде проверяй `m.IsValid()`.
@@TESTS
| `2 3` | `Result: 5\n` |
| `-1 1` | `Result: 0\n` |
| `10 20` | `Result: 30\n` |
@@CASES
run_case "2 3" $'Result: 5\n'
run_case "-1 1" $'Result: 0\n'
run_case "10 20" $'Result: 30\n'
@@MAIN
package main

import "fmt"

type Calculator struct{}

func (c Calculator) Add(a, b int) int {
	return a + b
}

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	// TODO: вызови Add через reflection
	_ = a
	_ = b
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"fmt"
	"reflect"
)

type Calculator struct{}

func (c Calculator) Add(a, b int) int {
	return a + b
}

func main() {
	var a, b int
	fmt.Scan(&a, &b)

	m := reflect.ValueOf(Calculator{}).MethodByName("Add")
	out := m.Call([]reflect.Value{reflect.ValueOf(a), reflect.ValueOf(b)})
	fmt.Printf("Result: %d\n", out[0].Int())
}
@@COMMENTED
package main

import (
	"fmt"
	"reflect"
)

type Calculator struct{}

func (c Calculator) Add(a, b int) int {
	return a + b
}

func main() {
	var a, b int
	fmt.Scan(&a, &b)

	// Находим метод по имени и вызываем с аргументами.
	m := reflect.ValueOf(Calculator{}).MethodByName("Add")
	out := m.Call([]reflect.Value{reflect.ValueOf(a), reflect.ValueOf(b)})
	fmt.Printf("Result: %d\n", out[0].Int())
}
@@END

@@TASK
section: 13_advanced
dir: 03_type_switch
num: 13_3
title: GO_13_03. Type switch
topics: `interface{}`, `type switch`, `strconv`
input: Одно слово
@@DESC
Считай слово и определи его тип: целое число, дробное число или строка.
Выведи одно из:

~~~text
int: 42
float: 3.50
string: hello
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 42 | int: 42 |
| 3.5 | float: 3.50 |
| hello | string: hello |
@@THEORY
## interface{}

~~~go
var v interface{}
v = 42        // int
v = 3.5       // float64
v = "hello"   // string
~~~

В `interface{}` (синоним `any`) можно положить значение любого типа.

## Type switch

~~~go
switch x := v.(type) {
case int:
    fmt.Printf("int: %d\n", x)
case float64:
    fmt.Printf("float: %.2f\n", x)
case string:
    fmt.Printf("string: %s\n", x)
}
~~~

В каждой ветке `x` уже имеет конкретный тип.

## Определение типа по строке

~~~go
if n, err := strconv.Atoi(s); err == nil {
    v = n
} else if f, err := strconv.ParseFloat(s, 64); err == nil {
    v = f
} else {
    v = s
}
~~~

Сначала пробуем целое, потом дробное, иначе оставляем строку.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `case float:` | Такого типа нет, нужен `float64` |
| Сравнение типов через `==` | Нужен type switch или `reflect` |
| `x` вне switch | Переменная из `case` видна только в ветке |
@@TESTS
| `42` | `int: 42\n` |
| `3.5` | `float: 3.50\n` |
| `hello` | `string: hello\n` |
| `-7` | `int: -7\n` |
@@CASES
run_case "42" $'int: 42\n'
run_case "3.5" $'float: 3.50\n'
run_case "hello" $'string: hello\n'
run_case "-7" $'int: -7\n'
@@MAIN
package main

import "fmt"

func main() {
	var s string
	fmt.Scan(&s)
	// TODO: определи тип и выведи значение
	_ = s
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

	var v interface{}
	if n, err := strconv.Atoi(s); err == nil {
		v = n
	} else if f, err := strconv.ParseFloat(s, 64); err == nil {
		v = f
	} else {
		v = s
	}

	switch x := v.(type) {
	case int:
		fmt.Printf("int: %d\n", x)
	case float64:
		fmt.Printf("float: %.2f\n", x)
	case string:
		fmt.Printf("string: %s\n", x)
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

	// Сначала целое, потом дробное, иначе строка.
	var v interface{}
	if n, err := strconv.Atoi(s); err == nil {
		v = n
	} else if f, err := strconv.ParseFloat(s, 64); err == nil {
		v = f
	} else {
		v = s
	}

	// В каждой ветке x уже конкретного типа.
	switch x := v.(type) {
	case int:
		fmt.Printf("int: %d\n", x)
	case float64:
		fmt.Printf("float: %.2f\n", x)
	case string:
		fmt.Printf("string: %s\n", x)
	}
}
@@END

@@TASK
section: 13_advanced
dir: 04_generics
num: 13_4
title: GO_13_04. Обобщённый Max
topics: дженерики, type parameters, `|`
input: Два числа
@@DESC
Напиши обобщённую функцию `Max[T int | float64](a, b T) T`, возвращающую
большее значение. Считай два дробных числа и выведи максимум:

~~~text
Max: 7.50
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 2.5 7.5 | Max: 7.50 |
| -1 -2 | Max: -1.00 |
@@THEORY
## Параметр типа

~~~go
func Max[T int | float64](a, b T) T {
    if a > b {
        return a
    }
    return b
}
~~~

`T` — параметр типа. `int | float64` — ограничение (constraint): `T` может
быть только одним из этих типов.

## Вызов

~~~go
fmt.Println(Max(3, 5))       // T = int
fmt.Println(Max(2.5, 7.5))   // T = float64
~~~

Тип выводится из аргументов, указывать его явно не нужно.

## Зачем

Одна реализация работает для нескольких типов без `interface{}` и приведения
типов. Проверка типов остаётся на этапе компиляции.

## Ограничения

Внутри функции доступны только операции, общие для всех типов ограничения.
Для чисел это обычно `+`, `-`, `*`, `<`, `>`.
@@TESTS
| `2.5 7.5` | `Max: 7.50\n` |
| `-1 -2` | `Max: -1.00\n` |
| `3 3` | `Max: 3.00\n` |
@@CASES
run_case "2.5 7.5" $'Max: 7.50\n'
run_case "-1 -2" $'Max: -1.00\n'
run_case "3 3" $'Max: 3.00\n'
@@MAIN
package main

import "fmt"

// TODO: сделай Max обобщённой
func Max[T int | float64](a, b T) T {
	return a
}

func main() {
	var a, b float64
	fmt.Scan(&a, &b)
	// TODO: выведи максимум
	_ = a
	_ = b
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func Max[T int | float64](a, b T) T {
	if a > b {
		return a
	}
	return b
}

func main() {
	var a, b float64
	fmt.Scan(&a, &b)
	fmt.Printf("Max: %.2f\n", Max(a, b))
}
@@COMMENTED
package main

import "fmt"

// Max работает для int и float64: тип T выводится из аргументов.
func Max[T int | float64](a, b T) T {
	if a > b {
		return a
	}
	return b
}

func main() {
	var a, b float64
	fmt.Scan(&a, &b)
	fmt.Printf("Max: %.2f\n", Max(a, b))
}
@@END
