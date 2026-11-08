@@TASK
section: 07_structs
dir: 01_first_struct
num: 7_1
title: GO_07_01. Первая структура
topics: структуры, поля, `fmt.Scan`
input: Два целых числа X и Y
@@DESC
Опиши структуру `Point` с полями `X` и `Y` типа `int`.
Считай два числа в поля структуры и выведи их:

~~~text
X: 3
Y: 4
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 3 4 | X: 3<br>Y: 4 |
| -1 0 | X: -1<br>Y: 0 |
@@THEORY
## Объявление структуры

~~~go
type Point struct {
    X int
    Y int
}
~~~

Структура — составной тип: несколько значений под одним именем.

## Создание и обращение к полям

~~~go
var p Point
fmt.Scan(&p.X, &p.Y)
fmt.Println(p.X, p.Y)
~~~

`fmt.Scan` умеет заполнять поля по указателям.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `type Point { X int }` | Забыто слово `struct` |
| `p.x` | Поле называется `X` |
| `fmt.Scan(p.X)` | Нужен адрес: `&p.X` |
@@TESTS
| `3 4` | `X: 3\nY: 4\n` |
| `-1 0` | `X: -1\nY: 0\n` |
| `0 0` | `X: 0\nY: 0\n` |
@@CASES
run_case "3 4" $'X: 3\nY: 4\n'
run_case "-1 0" $'X: -1\nY: 0\n'
run_case "0 0" $'X: 0\nY: 0\n'
@@MAIN
package main

import "fmt"

// TODO: объяви структуру Point

type Point struct {
	X int
	Y int
}

func main() {
	var p Point
	fmt.Scan(&p.X, &p.Y)
	// TODO: выведи поля в формате X: ... Y: ...
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

type Point struct {
	X int
	Y int
}

func main() {
	var p Point
	fmt.Scan(&p.X, &p.Y)
	fmt.Printf("X: %d\n", p.X)
	fmt.Printf("Y: %d\n", p.Y)
}
@@COMMENTED
package main

import "fmt"

// Point — точка на плоскости.
type Point struct {
	X int
	Y int
}

func main() {
	var p Point
	// Scan принимает указатели на поля.
	fmt.Scan(&p.X, &p.Y)
	fmt.Printf("X: %d\n", p.X)
	fmt.Printf("Y: %d\n", p.Y)
}
@@END

@@TASK
section: 07_structs
dir: 02_methods_area
num: 7_2
title: GO_07_02. Метод Area
topics: методы, получатель, `float64`
input: Ширина и высота прямоугольника
@@DESC
Опиши структуру `Rectangle` с полями `Width` и `Height`.
Добавь метод `Area() float64`, возвращающий площадь.
Считай два числа и выведи площадь с двумя знаками:

~~~text
Area: 10.00
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 2.5 4 | Area: 10.00 |
| 1 1 | Area: 1.00 |
@@THEORY
## Метод

~~~go
type Rectangle struct {
    Width  float64
    Height float64
}

func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}
~~~

`(r Rectangle)` — получатель. Внутри метода поля доступны как `r.Width`.

## Вызов

~~~go
r := Rectangle{Width: 2.5, Height: 4}
fmt.Printf("Area: %.2f\n", r.Area())
~~~

`%.2f` печатает число с двумя знаками после запятой.

## Указатель или значение

Для метода, который только читает поля, достаточно получателя-значения.
Получатель-указатель `(r *Rectangle)` нужен, если метод меняет структуру.
@@TESTS
| `2.5 4` | `Area: 10.00\n` |
| `1 1` | `Area: 1.00\n` |
| `0 5` | `Area: 0.00\n` |
| `3.5 2` | `Area: 7.00\n` |
@@CASES
run_case "2.5 4" $'Area: 10.00\n'
run_case "1 1" $'Area: 1.00\n'
run_case "0 5" $'Area: 0.00\n'
run_case "3.5 2" $'Area: 7.00\n'
@@MAIN
package main

import "fmt"

type Rectangle struct {
	Width  float64
	Height float64
}

// TODO: добавь метод Area() float64

func main() {
	var r Rectangle
	fmt.Scan(&r.Width, &r.Height)
	// TODO: выведи площадь
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

type Rectangle struct {
	Width  float64
	Height float64
}

func (r Rectangle) Area() float64 {
	return r.Width * r.Height
}

func main() {
	var r Rectangle
	fmt.Scan(&r.Width, &r.Height)
	fmt.Printf("Area: %.2f\n", r.Area())
}
@@COMMENTED
package main

import "fmt"

type Rectangle struct {
	Width  float64
	Height float64
}

// Area — метод с получателем-значением: структура не меняется.
func (r Rectangle) Area() float64 {
	return r.Width * r.Height
}

func main() {
	var r Rectangle
	fmt.Scan(&r.Width, &r.Height)
	fmt.Printf("Area: %.2f\n", r.Area())
}
@@END

@@TASK
section: 07_structs
dir: 03_constructor_new
num: 7_3
title: GO_07_03. Конструктор NewUser
topics: конструкторы, указатели, `New...`
input: Имя и возраст
@@DESC
Опиши структуру `User` с полями `Name string` и `Age int`.
Напиши функцию `NewUser(name string, age int) *User`, которая возвращает
указатель на новую структуру. Считай имя и возраст и выведи:

~~~text
Name: Alice, Age: 30
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| Alice 30 | Name: Alice, Age: 30 |
| Bob 18 | Name: Bob, Age: 18 |
@@THEORY
## Функция-конструктор

~~~go
type User struct {
    Name string
    Age  int
}

func NewUser(name string, age int) *User {
    return &User{Name: name, Age: age}
}
~~~

В Go нет конструкторов как в других языках. Вместо них пишут функцию
`NewXxx`, которая создаёт значение и возвращает его (часто указатель).

## Составной литерал

~~~go
u := User{Name: "Alice", Age: 30}
p := &User{Name: "Bob", Age: 18}
~~~

`&User{...}` создаёт структуру и сразу берёт её адрес.

## Зачем указатель

Указатель позволяет передавать структуру без копирования и менять её поля
в других функциях.
@@TESTS
| `Alice 30` | `Name: Alice, Age: 30\n` |
| `Bob 18` | `Name: Bob, Age: 18\n` |
| `Eve 0` | `Name: Eve, Age: 0\n` |
@@CASES
run_case "Alice 30" $'Name: Alice, Age: 30\n'
run_case "Bob 18" $'Name: Bob, Age: 18\n'
run_case "Eve 0" $'Name: Eve, Age: 0\n'
@@MAIN
package main

import "fmt"

type User struct {
	Name string
	Age  int
}

// TODO: напиши NewUser
func NewUser(name string, age int) *User {
	return &User{}
}

func main() {
	var name string
	var age int
	fmt.Scan(&name, &age)
	u := NewUser(name, age)
	// TODO: выведи Name и Age
	_ = u
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

type User struct {
	Name string
	Age  int
}

func NewUser(name string, age int) *User {
	return &User{Name: name, Age: age}
}

func main() {
	var name string
	var age int
	fmt.Scan(&name, &age)
	u := NewUser(name, age)
	fmt.Printf("Name: %s, Age: %d\n", u.Name, u.Age)
}
@@COMMENTED
package main

import "fmt"

type User struct {
	Name string
	Age  int
}

// NewUser — конструктор: создаёт User и возвращает указатель на него.
func NewUser(name string, age int) *User {
	return &User{Name: name, Age: age}
}

func main() {
	var name string
	var age int
	fmt.Scan(&name, &age)
	u := NewUser(name, age)
	// С указателем поля читаются так же: u.Name.
	fmt.Printf("Name: %s, Age: %d\n", u.Name, u.Age)
}
@@END

@@TASK
section: 07_structs
dir: 04_stringer
num: 7_4
title: GO_07_04. Интерфейс Stringer
topics: `String()`, `fmt.Stringer`, форматирование
input: Температура одним числом
@@DESC
Опиши тип `Temperature float64` и реализуй метод `String() string`,
который печатает температуру с двумя знаками и знаком градуса:

~~~text
Temp: 21.50°C
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 21.5 | Temp: 21.50°C |
| -5 | Temp: -5.00°C |
@@THEORY
## fmt.Stringer

~~~go
type Stringer interface {
    String() string
}
~~~

Если у типа есть метод `String() string`, `fmt` использует его при печати
через `%v`, `%s` и `Println`.

## Свой тип на основе float64

~~~go
type Temperature float64

func (t Temperature) String() string {
    return fmt.Sprintf("%.2f°C", float64(t))
}
~~~

Внутри метода приводим `t` к `float64`, потому что `Sprintf` ожидает обычное
число.

## Печать

~~~go
fmt.Printf("Temp: %v\n", t)
~~~

`%v` вызовет `String()` автоматически.
@@TESTS
| `21.5` | `Temp: 21.50°C\n` |
| `-5` | `Temp: -5.00°C\n` |
| `0` | `Temp: 0.00°C\n` |
@@CASES
run_case "21.5" $'Temp: 21.50°C\n'
run_case "-5" $'Temp: -5.00°C\n'
run_case "0" $'Temp: 0.00°C\n'
@@MAIN
package main

import "fmt"

type Temperature float64

// TODO: реализуй String() string

func main() {
	var t Temperature
	fmt.Scan(&t)
	// TODO: выведи температуру через %v
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

type Temperature float64

func (t Temperature) String() string {
	return fmt.Sprintf("%.2f°C", float64(t))
}

func main() {
	var t Temperature
	fmt.Scan(&t)
	fmt.Printf("Temp: %v\n", t)
}
@@COMMENTED
package main

import "fmt"

type Temperature float64

// String делает Temperature реализацией fmt.Stringer.
func (t Temperature) String() string {
	return fmt.Sprintf("%.2f°C", float64(t))
}

func main() {
	var t Temperature
	fmt.Scan(&t)
	// %v вызывает метод String.
	fmt.Printf("Temp: %v\n", t)
}
@@END

@@TASK
section: 07_structs
dir: 05_embedding
num: 7_5
title: GO_07_05. Встраивание структур
topics: встраивание, продвижение полей
input: Имя сотрудника и название компании
@@DESC
Опиши структуру `Person` с полем `Name`.
Опиши структуру `Employee`, которая **встраивает** `Person` и добавляет поле
`Company`. Считай два слова и выведи:

~~~text
Name: Bob, Company: Acme
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| Bob Acme | Name: Bob, Company: Acme |
| Ann Globex | Name: Ann, Company: Globex |
@@THEORY
## Встраивание

~~~go
type Person struct {
    Name string
}

type Employee struct {
    Person
    Company string
}
~~~

Поле `Person` записано без имени — это встраивание (embedding).

## Продвижение полей

~~~go
e := Employee{Person: Person{Name: "Bob"}, Company: "Acme"}
fmt.Println(e.Name)      // Bob
fmt.Println(e.Person.Name) // тоже Bob
~~~

Поле `Name` «продвигается» наверх: к нему можно обращаться напрямую.

## Зачем это нужно

Встраивание заменяет наследование: `Employee` получает поля и методы
`Person`, но остаётся отдельным типом.
@@TESTS
| `Bob Acme` | `Name: Bob, Company: Acme\n` |
| `Ann Globex` | `Name: Ann, Company: Globex\n` |
@@CASES
run_case "Bob Acme" $'Name: Bob, Company: Acme\n'
run_case "Ann Globex" $'Name: Ann, Company: Globex\n'
run_case "Eve Initech" $'Name: Eve, Company: Initech\n'
@@MAIN
package main

import "fmt"

type Person struct {
	Name string
}

// TODO: опиши Employee со встроенным Person и полем Company

type Employee struct {
	Person
	Company string
}

func main() {
	var e Employee
	fmt.Scan(&e.Name, &e.Company)
	// TODO: выведи имя и компанию
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

type Person struct {
	Name string
}

type Employee struct {
	Person
	Company string
}

func main() {
	var e Employee
	fmt.Scan(&e.Name, &e.Company)
	fmt.Printf("Name: %s, Company: %s\n", e.Name, e.Company)
}
@@COMMENTED
package main

import "fmt"

type Person struct {
	Name string
}

// Employee встраивает Person: поле Name доступно напрямую.
type Employee struct {
	Person
	Company string
}

func main() {
	var e Employee
	fmt.Scan(&e.Name, &e.Company)
	fmt.Printf("Name: %s, Company: %s\n", e.Name, e.Company)
}
@@END

@@TASK
section: 07_structs
dir: 06_interfaces
num: 7_6
title: GO_07_06. Интерфейс Shape
topics: интерфейсы, полиморфизм, `math.Pi`
input: Радиус круга и сторона квадрата
@@DESC
Опиши интерфейс `Shape` с методом `Area() float64`.
Реализуй его для `Circle` (поле `R`) и `Square` (поле `Side`).
Положи обе фигуры в срез `[]Shape`, посчитай суммарную площадь и выведи:

~~~text
Total: 21.57
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 2 3 | Total: 21.57 |
| 1 1 | Total: 4.14 |
@@THEORY
## Интерфейс

~~~go
type Shape interface {
    Area() float64
}
~~~

Тип реализует интерфейс, если у него есть все методы интерфейса. Слово
`implements` писать не нужно.

## Две реализации

~~~go
type Circle struct{ R float64 }
func (c Circle) Area() float64 { return math.Pi * c.R * c.R }

type Square struct{ Side float64 }
func (s Square) Area() float64 { return s.Side * s.Side }
~~~

## Полиморфизм

~~~go
shapes := []Shape{Circle{R: 2}, Square{Side: 3}}
total := 0.0
for _, s := range shapes {
    total += s.Area()
}
~~~

Цикл вызывает `Area` у конкретного типа, лежащего в переменной интерфейса.
@@TESTS
| `2 3` | `Total: 21.57\n` |
| `1 1` | `Total: 4.14\n` |
| `0 2` | `Total: 4.00\n` |
@@CASES
run_case "2 3" $'Total: 21.57\n'
run_case "1 1" $'Total: 4.14\n'
run_case "0 2" $'Total: 4.00\n'
@@MAIN
package main

import "fmt"

// TODO: объяви интерфейс Shape

type Shape interface {
	Area() float64
}

type Circle struct{ R float64 }

type Square struct{ Side float64 }

// TODO: реализуй Area для обеих фигур
func (c Circle) Area() float64 { return 0 }

func (s Square) Area() float64 { return 0 }

func main() {
	var r, side float64
	fmt.Scan(&r, &side)
	shapes := []Shape{Circle{R: r}, Square{Side: side}}
	total := 0.0
	for _, s := range shapes {
		total += s.Area()
	}
	fmt.Printf("Total: %.2f\n", total)
}
@@SOLUTION
package main

import (
	"fmt"
	"math"
)

type Shape interface {
	Area() float64
}

type Circle struct{ R float64 }

type Square struct{ Side float64 }

func (c Circle) Area() float64 {
	return math.Pi * c.R * c.R
}

func (s Square) Area() float64 {
	return s.Side * s.Side
}

func main() {
	var r, side float64
	fmt.Scan(&r, &side)
	shapes := []Shape{Circle{R: r}, Square{Side: side}}
	total := 0.0
	for _, s := range shapes {
		total += s.Area()
	}
	fmt.Printf("Total: %.2f\n", total)
}
@@COMMENTED
package main

import (
	"fmt"
	"math"
)

// Shape — всё, у чего есть площадь.
type Shape interface {
	Area() float64
}

type Circle struct{ R float64 }

type Square struct{ Side float64 }

func (c Circle) Area() float64 {
	return math.Pi * c.R * c.R
}

func (s Square) Area() float64 {
	return s.Side * s.Side
}

func main() {
	var r, side float64
	fmt.Scan(&r, &side)
	// В срезе интерфейсов могут лежать значения разных типов.
	shapes := []Shape{Circle{R: r}, Square{Side: side}}
	total := 0.0
	for _, s := range shapes {
		total += s.Area()
	}
	fmt.Printf("Total: %.2f\n", total)
}
@@END

@@TASK
section: 08_maps
dir: 01_word_count
num: 8_1
title: GO_08_01. Подсчёт слов через map
topics: `map`, `strings.Fields`, сортировка ключей
input: Одна строка со словами
@@DESC
Посчитай, сколько раз встречается каждое слово. Выведи слова в алфавитном
порядке в формате `слово: количество`:

~~~text
apple: 2
banana: 1
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| apple banana apple | apple: 2<br>banana: 1 |
| a | a: 1 |
@@THEORY
## Создание и запись

~~~go
counts := make(map[string]int)
for _, w := range strings.Fields(line) {
    counts[w]++
}
~~~

Если ключа нет, `counts[w]` возвращает нулевое значение `0`, поэтому `++`
работает сразу.

## Сортировка ключей

Порядок обхода `map` в Go **не определён**. Чтобы вывод был стабильным,
собери ключи в срез и отсортируй:

~~~go
keys := make([]string, 0, len(counts))
for k := range counts {
    keys = append(keys, k)
}
sort.Strings(keys)
~~~

## Печать

~~~go
for _, k := range keys {
    fmt.Printf("%s: %d\n", k, counts[k])
}
~~~
@@TESTS
| `apple banana apple` | `apple: 2\nbanana: 1\n` |
| `a` | `a: 1\n` |
| `b a b a b` | `a: 2\nb: 3\n` |
@@CASES
run_case "apple banana apple" $'apple: 2\nbanana: 1\n'
run_case "a" $'a: 1\n'
run_case "b a b a b" $'a: 2\nb: 3\n'
run_case "" ""
@@MAIN
package main

import (
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	data, _ := io.ReadAll(os.Stdin)
	line := strings.TrimSpace(string(data))
	// TODO: посчитай слова и выведи по алфавиту
	_ = line
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"fmt"
	"io"
	"os"
	"sort"
	"strings"
)

func main() {
	data, _ := io.ReadAll(os.Stdin)
	line := strings.TrimSpace(string(data))
	counts := make(map[string]int)
	for _, w := range strings.Fields(line) {
		counts[w]++
	}
	keys := make([]string, 0, len(counts))
	for k := range counts {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	for _, k := range keys {
		fmt.Printf("%s: %d\n", k, counts[k])
	}
}
@@COMMENTED
package main

import (
	"fmt"
	"io"
	"os"
	"sort"
	"strings"
)

func main() {
	data, _ := io.ReadAll(os.Stdin)
	line := strings.TrimSpace(string(data))

	counts := make(map[string]int)
	for _, w := range strings.Fields(line) {
		// Если ключа ещё нет, counts[w] равен 0.
		counts[w]++
	}

	// Порядок обхода map не определён — сортируем ключи.
	keys := make([]string, 0, len(counts))
	for k := range counts {
		keys = append(keys, k)
	}
	sort.Strings(keys)

	for _, k := range keys {
		fmt.Printf("%s: %d\n", k, counts[k])
	}
}
@@END

@@TASK
section: 08_maps
dir: 02_map_comma_ok
num: 8_2
title: GO_08_02. Идиома comma-ok
topics: `map`, `comma ok`, отличие нулевого значения
input: Число N, затем N пар «ключ значение», затем ключ для поиска
@@DESC
Считай `N`, затем `N` пар «слово число». Сохрани их в `map[string]int`.
Затем считай слово для поиска. Если оно есть в map — выведи число, иначе
выведи `NOT FOUND`.

~~~text
7
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 3<br>cat 5<br>dog 7<br>fish 2<br>dog | 7 |
| 1<br>a 0<br>a | 0 |
| 1<br>a 1<br>b | NOT FOUND |
@@THEORY
## Проблема нулевого значения

~~~go
v := m["missing"] // v == 0
~~~

Нельзя понять, лежит в map ноль или ключа вообще нет.

## Идиома comma-ok

~~~go
v, ok := m["dog"]
if ok {
    fmt.Println(v)
} else {
    fmt.Println("NOT FOUND")
}
~~~

Второе значение — `bool`: был ли ключ найден.

## Чтение пар

~~~go
m := make(map[string]int)
for i := 0; i < n; i++ {
    var key string
    var value int
    fmt.Scan(&key, &value)
    m[key] = value
}
~~~
@@TESTS
| `3\ncat 5\ndog 7\nfish 2\ndog` | `7\n` |
| `1\na 0\na` | `0\n` |
| `1\na 1\nb` | `NOT FOUND\n` |
| `2\nx -1\ny 4\ny` | `4\n` |
@@CASES
run_case $'3\ncat 5\ndog 7\nfish 2\ndog' $'7\n'
run_case $'1\na 0\na' $'0\n'
run_case $'1\na 1\nb' $'NOT FOUND\n'
run_case $'2\nx -1\ny 4\ny' $'4\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	m := make(map[string]int)
	for i := 0; i < n; i++ {
		var key string
		var value int
		fmt.Scan(&key, &value)
		m[key] = value
	}
	var query string
	fmt.Scan(&query)
	// TODO: используй comma-ok
	fmt.Println("TODO")
}
@@SOLUTION
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	m := make(map[string]int)
	for i := 0; i < n; i++ {
		var key string
		var value int
		fmt.Scan(&key, &value)
		m[key] = value
	}
	var query string
	fmt.Scan(&query)
	if v, ok := m[query]; ok {
		fmt.Println(v)
	} else {
		fmt.Println("NOT FOUND")
	}
}
@@COMMENTED
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	m := make(map[string]int)
	for i := 0; i < n; i++ {
		var key string
		var value int
		fmt.Scan(&key, &value)
		m[key] = value
	}

	var query string
	fmt.Scan(&query)
	// ok == true, только если ключ действительно есть в map.
	if v, ok := m[query]; ok {
		fmt.Println(v)
	} else {
		fmt.Println("NOT FOUND")
	}
}
@@END

@@TASK
section: 08_maps
dir: 03_unique_elements
num: 8_3
title: GO_08_03. Уникальные элементы
topics: `map[int]bool`, множество, `sort.Ints`
input: Число N, затем N целых чисел
@@DESC
Найди уникальные числа, выведи их количество и сами числа по возрастанию:

~~~text
Unique: 4
1 2 3 4
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 6<br>3 1 3 2 1 4 | Unique: 4<br>1 2 3 4 |
| 2<br>5 5 | Unique: 1<br>5 |
| 1<br>-1 | Unique: 1<br>-1 |
@@THEORY
## Множество на map

В Go нет отдельного типа `set`. Его заменяет `map[T]bool`:

~~~go
seen := make(map[int]bool)
seen[3] = true
if seen[3] {
    // элемент уже встречался
}
~~~

## Сбор уникальных

~~~go
unique := make([]int, 0)
for _, x := range numbers {
    if !seen[x] {
        seen[x] = true
        unique = append(unique, x)
    }
}
sort.Ints(unique)
~~~

## Вывод среза

~~~go
parts := make([]string, len(unique))
for i, x := range unique {
    parts[i] = fmt.Sprint(x)
}
fmt.Println(strings.Join(parts, " "))
~~~
@@TESTS
| `6\n3 1 3 2 1 4` | `Unique: 4\n1 2 3 4\n` |
| `2\n5 5` | `Unique: 1\n5\n` |
| `1\n-1` | `Unique: 1\n-1\n` |
| `0` | `Unique: 0\n\n` |
@@CASES
run_case $'6\n3 1 3 2 1 4' $'Unique: 4\n1 2 3 4\n'
run_case $'2\n5 5' $'Unique: 1\n5\n'
run_case $'1\n-1' $'Unique: 1\n-1\n'
run_case "0" $'Unique: 0\n\n'
@@MAIN
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// TODO: собери уникальные числа, отсортируй и выведи
	_ = n
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	seen := make(map[int]bool)
	unique := make([]int, 0)
	for i := 0; i < n; i++ {
		var x int
		fmt.Scan(&x)
		if !seen[x] {
			seen[x] = true
			unique = append(unique, x)
		}
	}
	sort.Ints(unique)
	parts := make([]string, len(unique))
	for i, x := range unique {
		parts[i] = fmt.Sprint(x)
	}
	fmt.Printf("Unique: %d\n", len(unique))
	fmt.Println(strings.Join(parts, " "))
}
@@COMMENTED
package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)

	// map[int]bool работает как множество.
	seen := make(map[int]bool)
	unique := make([]int, 0)
	for i := 0; i < n; i++ {
		var x int
		fmt.Scan(&x)
		if !seen[x] {
			seen[x] = true
			unique = append(unique, x)
		}
	}

	sort.Ints(unique)
	parts := make([]string, len(unique))
	for i, x := range unique {
		parts[i] = fmt.Sprint(x)
	}
	fmt.Printf("Unique: %d\n", len(unique))
	fmt.Println(strings.Join(parts, " "))
}
@@END

@@TASK
section: 08_maps
dir: 04_group_by_length
num: 8_4
title: GO_08_04. Группировка по длине
topics: `map[int][]string`, вложенные срезы, сортировка
input: Одна строка со словами
@@DESC
Сгруппируй слова по длине. Выведи группы по возрастанию длины, слова внутри
группы — по алфавиту:

~~~text
1: a
3: bee cat dog
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| a cat dog bee | 1: a<br>3: bee cat dog |
| go | 2: go |
@@THEORY
## Map со срезом в значении

~~~go
groups := make(map[int][]string)
for _, w := range words {
    n := len([]rune(w))
    groups[n] = append(groups[n], w)
}
~~~

Значение map — срез, поэтому `append` дописывает слово в нужную группу.

## Сортировка

~~~go
lengths := make([]int, 0, len(groups))
for n := range groups {
    lengths = append(lengths, n)
}
sort.Ints(lengths)
for _, n := range lengths {
    sort.Strings(groups[n])
}
~~~

## Длина в рунах

`len(w)` считает байты. Для кириллицы правильнее `len([]rune(w))`.
@@TESTS
| `a cat dog bee` | `1: a\n3: bee cat dog\n` |
| `go` | `2: go\n` |
| `dd cc a bbb` | `1: a\n2: cc dd\n3: bbb\n` |
@@CASES
run_case "a cat dog bee" $'1: a\n3: bee cat dog\n'
run_case "go" $'2: go\n'
run_case "dd cc a bbb" $'1: a\n2: cc dd\n3: bbb\n'
@@MAIN
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
	// TODO: сгруппируй слова по длине
	_ = words
	fmt.Println("TODO")
}
@@SOLUTION
package main

import (
	"fmt"
	"io"
	"os"
	"sort"
	"strings"
)

func main() {
	data, _ := io.ReadAll(os.Stdin)
	words := strings.Fields(string(data))

	groups := make(map[int][]string)
	for _, w := range words {
		n := len([]rune(w))
		groups[n] = append(groups[n], w)
	}

	lengths := make([]int, 0, len(groups))
	for n := range groups {
		lengths = append(lengths, n)
	}
	sort.Ints(lengths)

	for _, n := range lengths {
		sort.Strings(groups[n])
		fmt.Printf("%d: %s\n", n, strings.Join(groups[n], " "))
	}
}
@@COMMENTED
package main

import (
	"fmt"
	"io"
	"os"
	"sort"
	"strings"
)

func main() {
	data, _ := io.ReadAll(os.Stdin)
	words := strings.Fields(string(data))

	// Ключ — длина слова, значение — срез слов этой длины.
	groups := make(map[int][]string)
	for _, w := range words {
		n := len([]rune(w))
		groups[n] = append(groups[n], w)
	}

	lengths := make([]int, 0, len(groups))
	for n := range groups {
		lengths = append(lengths, n)
	}
	sort.Ints(lengths)

	for _, n := range lengths {
		sort.Strings(groups[n])
		fmt.Printf("%d: %s\n", n, strings.Join(groups[n], " "))
	}
}
@@END

@@TASK
section: 08_maps
dir: 05_invert_map
num: 8_5
title: GO_08_05. Инверсия map
topics: `map`, `strconv.Atoi`, сортировка числовых ключей
input: Число N, затем N пар «слово число»
@@DESC
Считай `N` пар «слово число» в `map[string]int`, затем построй обратную
map `map[int]string`. Выведи пары по возрастанию числа:

~~~text
1: a
2: b
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| 3<br>a 1<br>b 2<br>c 3 | 1: a<br>2: b<br>3: c |
| 2<br>z 10<br>y 5 | 5: y<br>10: z |
@@THEORY
## Инверсия

~~~go
direct := map[string]int{"a": 1, "b": 2}
inverse := make(map[int]string)
for word, num := range direct {
    inverse[num] = word
}
~~~

Ключи и значения меняются местами. Такая операция корректна, только если
значения уникальны.

## Числовая сортировка ключей

`sort.Strings` отсортировал бы `"10"` раньше `"5"`. Для чисел собираем срез
`[]int` и вызываем `sort.Ints`:

~~~go
nums := make([]int, 0, len(inverse))
for n := range inverse {
    nums = append(nums, n)
}
sort.Ints(nums)
~~~

## Вывод

~~~go
for _, n := range nums {
    fmt.Printf("%d: %s\n", n, inverse[n])
}
~~~
@@TESTS
| `3\na 1\nb 2\nc 3` | `1: a\n2: b\n3: c\n` |
| `2\nz 10\ny 5` | `5: y\n10: z\n` |
| `1\nsolo 42` | `42: solo\n` |
@@CASES
run_case $'3\na 1\nb 2\nc 3' $'1: a\n2: b\n3: c\n'
run_case $'2\nz 10\ny 5' $'5: y\n10: z\n'
run_case $'1\nsolo 42' $'42: solo\n'
@@MAIN
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
@@SOLUTION
package main

import (
	"fmt"
	"sort"
)

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

	inverse := make(map[int]string)
	for word, num := range direct {
		inverse[num] = word
	}

	nums := make([]int, 0, len(inverse))
	for num := range inverse {
		nums = append(nums, num)
	}
	sort.Ints(nums)

	for _, num := range nums {
		fmt.Printf("%d: %s\n", num, inverse[num])
	}
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
	direct := make(map[string]int)
	for i := 0; i < n; i++ {
		var word string
		var num int
		fmt.Scan(&word, &num)
		direct[word] = num
	}

	// Меняем ключи и значения местами.
	inverse := make(map[int]string)
	for word, num := range direct {
		inverse[num] = word
	}

	nums := make([]int, 0, len(inverse))
	for num := range inverse {
		nums = append(nums, num)
	}
	sort.Ints(nums)

	for _, num := range nums {
		fmt.Printf("%d: %s\n", num, inverse[num])
	}
}
@@END
