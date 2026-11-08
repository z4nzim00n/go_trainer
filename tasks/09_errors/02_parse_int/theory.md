# Разбор задания

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
