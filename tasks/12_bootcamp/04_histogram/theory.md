# Разбор задания

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
