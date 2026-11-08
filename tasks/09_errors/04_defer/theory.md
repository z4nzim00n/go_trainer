# Разбор задания

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
