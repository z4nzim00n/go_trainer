# Разбор задания

## Вложенные срезы

~~~go
matrix := make([][]int, rows)
for i := range matrix {
    matrix[i] = make([]int, cols)
    for j := range matrix[i] {
        fmt.Scan(&matrix[i][j])
    }
}
~~~

`make([][]int, rows)` создаёт срез строк, каждую строку нужно создать отдельно.

## Обход

~~~go
sum := 0
for _, row := range matrix {
    for _, x := range row {
        sum += x
    }
}
~~~

Внешний цикл идёт по строкам, внутренний — по элементам строки.

## Почему не make([][]int, rows, cols)

Второй аргумент — длина внешнего среза. Он не задаёт длину вложенных срезов.
