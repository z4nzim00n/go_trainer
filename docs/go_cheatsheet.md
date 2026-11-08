# Шпаргалка по Go

Краткий справочник по темам тренажёра. Синтаксис — Go 1.18+.

---

## 1. Структура программы

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, Go!")
}
```

- `package main` + `func main()` — исполняемая программа.
- Импорт нескольких пакетов:

```go
import (
    "fmt"
    "strings"
)
```

- Неиспользуемый импорт или локальная переменная — **ошибка компиляции**.
- Точка с запятой не нужна, `gofmt` расставляет отступы.

Запуск одного файла:

```bash
go run main.go
go build -o app.exe main.go
```

---

## 2. Переменные и типы

```go
var x int          // 0
var s string       // ""
var ok bool        // false
var p *int         // nil

y := 42            // короткое объявление, только внутри функций
a, b := 1, 2       // несколько переменных
const Pi = 3.14159
```

Основные типы:

| Тип | Размер | Нулевое значение |
| --- | --- | --- |
| `int` | 32/64 бита (платформа) | `0` |
| `int8/16/32/64` | 8/16/32/64 бита | `0` |
| `uint`, `uint8`… | беззнаковые | `0` |
| `float32`, `float64` | 4/8 байт | `0` |
| `bool` | — | `false` |
| `string` | UTF-8 байты | `""` |
| `rune` | псевдоним `int32` | `0` |
| `byte` | псевдоним `uint8` | `0` |

Приведение:

```go
n := 42
f := float64(n)
i := int(3.9) // 3, дробная часть отбрасывается
s := strconv.Itoa(n)
n2, err := strconv.Atoi("42")
```

---

## 3. Ввод и вывод

```go
var x int
fmt.Scan(&x)              // нужен указатель

var name string
fmt.Scan(&name)           // читает до пробела

fmt.Println("x =", x)     // добавляет \n
fmt.Print(x)              // без \n
fmt.Printf("%d %.2f %s\n", 42, 3.5, "ok")
```

Глаголы:

| Глагол | Значение |
| --- | --- |
| `%d` | целое |
| `%f`, `%.2f` | дробное, 2 знака |
| `%s` | строка |
| `%v` | значение по умолчанию |
| `%T` | тип значения |
| `%q` | строка в кавычках |

Чтение строки целиком:

```go
scanner := bufio.NewScanner(os.Stdin)
for scanner.Scan() {
    line := scanner.Text()
    fmt.Println(line)
}
```

Или весь stdin:

```go
data, _ := io.ReadAll(os.Stdin)
text := string(data)
```

---

## 4. Арифметика и условия

```go
7 / 2        // 3
7 % 2        // 1
-7 % 2       // -1
7.0 / 2      // 3.5
math.Pi
```

`%` работает только для целых. Для дробных — `math.Mod`.

```go
if x > 0 {
    // ...
} else if x == 0 {
    // ...
} else {
    // ...
}

switch day {
case "sat", "sun":
    fmt.Println("weekend")
default:
    fmt.Println("workday")
}
```

В Go нет тернарного оператора.

---

## 5. Циклы

```go
for i := 0; i < 5; i++ {
    fmt.Println(i)
}

n := 5
for n > 0 {
    n--
}

for {          // бесконечный
    break
}

numbers := []int{10, 20, 30}
for i, v := range numbers {
    fmt.Println(i, v)
}
```

`range` по строке даёт **индекс байта** и **rune**:

```go
for i, r := range "привет" {
    fmt.Println(i, string(r))
}
```

`break` выходит из цикла, `continue` переходит к следующей итерации.

---

## 6. Срезы

```go
a := []int{1, 2, 3}       // срез
b := [3]int{1, 2, 3}      // массив

s := make([]int, 3)       // len=3, cap=3
s := make([]int, 0, 10)   // len=0, cap=10

s = append(s, 4)
fmt.Println(len(s), cap(s))

part := s[1:3]            // элементы 1 и 2
copy(dst, src)

sort.Ints(s)
sort.Strings(words)
```

- Срез — дескриптор: указатель на массив, `len`, `cap`.
- Присваивание среза копирует дескриптор, а не данные.
- `append` может выделить новый массив.
- `nil`-срез можно читать (`len == 0`) и в него можно делать `append`.

Вывод среза через пробел:

```go
parts := make([]string, len(s))
for i, x := range s {
    parts[i] = fmt.Sprint(x)
}
fmt.Println(strings.Join(parts, " "))
```

---

## 7. Строки и руны

Строки неизменяемы. `len(s)` — байты, `utf8.RuneCountInString(s)` — символы.

```go
s := "Привет"

strings.ToUpper(s)
strings.ToLower(s)
strings.TrimSpace(s)
strings.Fields(s)              // по любым пробельным символам
strings.Join(words, " ")
strings.Split(s, ",")
strings.Contains(s, "ри")
strings.HasPrefix(s, "Пр")
strings.Repeat("*", 3)
```

Разворот строки по рунам:

```go
r := []rune(s)
for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
    r[i], r[j] = r[j], r[i]
}
fmt.Println(string(r))
```

Сборка:

```go
var b strings.Builder
b.WriteString("a")
b.WriteString("b")
fmt.Println(b.String())
```

---

## 8. Структуры и методы

```go
type Point struct {
    X int
    Y int
}

p := Point{X: 1, Y: 2}
p.X = 10
```

Методы:

```go
func (p Point) Sum() int {
    return p.X + p.Y
}

func (p *Point) Move(dx int) {
    p.X += dx
}
```

- Получатель-значение работает с копией.
- Получатель-указатель меняет оригинал.

Встраивание:

```go
type Person struct{ Name string }

type Employee struct {
    Person
    Company string
}

e := Employee{Person: Person{Name: "Bob"}, Company: "Acme"}
fmt.Println(e.Name) // Bob
```

Интерфейсы:

```go
type Shape interface {
    Area() float64
}

func (c Circle) Area() float64 { return math.Pi * c.R * c.R }
```

Реализация неявная: достаточно иметь все методы.

`String() string` — реализация `fmt.Stringer`, используется `%v`.

---

## 9. Map

```go
m := make(map[string]int)
m["a"] = 1
m["a"]++

v := m["missing"]       // 0
v, ok := m["a"]         // comma-ok
delete(m, "a")
```

Обход:

```go
for k, v := range m {
    fmt.Println(k, v)
}
```

Порядок обхода не определён. Для стабильного вывода сортируй ключи.

Множество:

```go
seen := make(map[int]bool)
seen[x] = true
```

Ключ должен быть сравним: числа, строки, структуры из сравнимых полей.
Срез, map и функция ключами быть не могут.

---

## 10. Ошибки, defer, panic

```go
func Divide(a, b int) (int, error) {
    if b == 0 {
        return 0, errors.New("division by zero")
    }
    return a / b, nil
}

result, err := Divide(10, 2)
if err != nil {
    fmt.Println("Error:", err)
} else {
    fmt.Println(result)
}
```

Своя ошибка:

```go
type ValidationError struct{ Field string }

func (e *ValidationError) Error() string {
    return "validation failed: " + e.Field
}
```

`defer` выполняет вызов при выходе из функции, несколько `defer` — LIFO:

```go
func process() {
    defer fmt.Println("close")
    fmt.Println("work")
}
```

`panic` + `recover`:

```go
func safe(a, b int) (result int, err error) {
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
```

`errors.Is` и `errors.As`:

```go
if errors.Is(err, os.ErrNotExist) { ... }

var ve *ValidationError
if errors.As(err, &ve) { ... }
```

---

## 11. Файлы

```go
data, err := os.ReadFile("input.txt")
if err != nil {
    fmt.Println("Error:", err)
    return
}
fmt.Print(string(data))

err = os.WriteFile("out.txt", []byte("hello\n"), 0644)
```

Построчное чтение:

```go
f, err := os.Open("input.txt")
if err != nil { return }
defer f.Close()

scanner := bufio.NewScanner(f)
for scanner.Scan() {
    fmt.Println(scanner.Text())
}
```

Проверка существования:

```go
if errors.Is(err, os.ErrNotExist) { ... }
```

---

## 12. Горутины и каналы

```go
go func() {
    fmt.Println("worker")
}()
```

Небуферизованный канал синхронизирует отправителя и получателя:

```go
ch := make(chan int)
go func() { ch <- 42 }()
fmt.Println(<-ch)
```

Буферизованный:

```go
ch := make(chan int, 2)
ch <- 1
ch <- 2
close(ch)

for v := range ch {
    fmt.Println(v)
}
```

`sync.Mutex`:

```go
var mu sync.Mutex
mu.Lock()
counter++
mu.Unlock()
```

`sync.WaitGroup`:

```go
var wg sync.WaitGroup
wg.Add(1)
go func() {
    defer wg.Done()
    // работа
}()
wg.Wait()
```

Правила:

- закрывает канал отправитель, не получатель;
- запись в закрытый канал — паника;
- чтение из закрытого канала возвращает нулевое значение и `ok == false`;
- `range` завершается после закрытия и опустошения канала.

Проверка гонок:

```bash
go run -race main.go
```

---

## 13. Reflection и дженерики

Reflection:

```go
v := reflect.ValueOf(p)
t := v.Type()

for i := 0; i < t.NumField(); i++ {
    fmt.Println(t.Field(i).Name, v.Field(i).Interface())
}

m := reflect.ValueOf(obj).MethodByName("Add")
out := m.Call([]reflect.Value{reflect.ValueOf(1), reflect.ValueOf(2)})
fmt.Println(out[0].Int())
```

Type switch:

```go
switch x := v.(type) {
case int:
    fmt.Println("int", x)
case float64:
    fmt.Println("float", x)
case string:
    fmt.Println("string", x)
}
```

Дженерики:

```go
func Max[T int | float64](a, b T) T {
    if a > b {
        return a
    }
    return b
}

fmt.Println(Max(2.5, 7.5))
```

`any` — псевдоним `interface{}`.

---

## 14. Полезные пакеты

| Пакет | Для чего |
| --- | --- |
| `fmt` | ввод и вывод |
| `os` | файлы, stdin/stdout, аргументы |
| `io` | `ReadAll`, интерфейсы Reader/Writer |
| `bufio` | построчное чтение |
| `strings` | работа со строками |
| `strconv` | преобразование строк и чисел |
| `sort` | сортировка срезов |
| `math` | `Pi`, `Sqrt`, `Abs` |
| `errors` | создание и разбор ошибок |
| `sync` | Mutex, WaitGroup |
| `reflect` | runtime-информация о типах |
| `time` | время и таймеры |
| `unicode/utf8` | подсчёт рун |

---

## 15. Частые ошибки новичка

| Ошибка | Как правильно |
| --- | --- |
| `fmt.Scan(x)` | `fmt.Scan(&x)` |
| `7 / 2` для среднего | `float64(sum) / float64(n)` |
| `len("привет")` как число букв | `utf8.RuneCountInString(s)` |
| Запись в `nil`-map | `make(map[K]V)` |
| `map` без сортировки ключей | собрать ключи и `sort` |
| Игнорирование `err` | проверять сразу |
| `defer` в цикле без причины | закрывать ресурс в функции |
| Гонка счётчика | `Mutex` или канал |
| Сравнение строк через `==` в C-стиле | в Go `==` как раз сравнивает содержимое |
| `%` для `float64` | `math.Mod` |
